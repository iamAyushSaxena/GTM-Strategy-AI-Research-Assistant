"""
Visualization Module
Creates charts and visualizations for GTM strategy
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from typing import Dict, List
from config import *

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10


class GTMVisualizer:
    """
    Creates visualizations for GTM strategy presentation
    """
    
    def __init__(self):
        self.colors = COLOR_SCHEME
        
    def plot_positioning_matrix(self, positioning_data: pd.DataFrame) -> go.Figure:
        """
        Create interactive positioning matrix
        """
        print("📍 Creating positioning matrix...")
        
        fig = go.Figure()
        
        # 1. Add "Our Product" FIRST (So it's top of the legend)
        our_product = positioning_data[positioning_data['is_our_product']]
        fig.add_trace(go.Scatter(
            x=our_product['x_specialization'],
            y=our_product['y_user_type'],
            mode='markers+text',
            name='Our Product',
            text=our_product['label'],
            textposition='top center',
            marker=dict(
                size=25,
                color=self.colors['accent'],
                symbol='star',
                line=dict(color='white', width=3)
            ),
            hovertemplate='<b>%{text}</b><br>Specialization: %{x}<br>User Type: %{y}<extra></extra>'
        ))
        
        # 2. Add Competitors SECOND
        competitors = positioning_data[~positioning_data['is_our_product']]
        fig.add_trace(go.Scatter(
            x=competitors['x_specialization'],
            y=competitors['y_user_type'],
            mode='markers+text',
            name='Competitors',
            text=competitors['label'],
            textposition='top center',
            marker=dict(
                size=15,
                color=self.colors['secondary'],
                line=dict(color='white', width=2)
            ),
            hovertemplate='<b>%{text}</b><br>Specialization: %{x}<br>User Type: %{y}<extra></extra>'
        ))
        
        # Add quadrant lines
        fig.add_hline(y=5, line_dash="dash", line_color="gray", opacity=0.3)
        fig.add_vline(x=5, line_dash="dash", line_color="gray", opacity=0.3)
        
        # Add Quadrant Labels (In Corners)
        # Top-Left
        fig.add_annotation(
            x=0.5, y=9.5, 
            text="Generalist<br>Team", 
            showarrow=False,
            font=dict(size=14, color="gray", weight="bold"), 
            opacity=0.4,
            xanchor="left", yanchor="top"
        )
        # Top-Right
        fig.add_annotation(
            x=9.5, y=9.5, 
            text="Specialist<br>Team", 
            showarrow=False,
            font=dict(size=14, color="gray", weight="bold"), 
            opacity=0.4,
            xanchor="right", yanchor="top"
        )
        # Bottom-Left
        fig.add_annotation(
            x=0.5, y=0.5, 
            text="Generalist<br>Individual", 
            showarrow=False,
            font=dict(size=14, color="gray", weight="bold"), 
            opacity=0.4,
            xanchor="left", yanchor="bottom"
        )
        # Bottom-Right (White Space)
        fig.add_annotation(
            x=9.5, y=0.5, 
            text="Specialist<br>Individual<br>(WHITE SPACE)", 
            showarrow=False,
            font=dict(size=14, color=self.colors['success'], weight="bold"), 
            opacity=0.8,
            xanchor="right", yanchor="bottom"
        )
        
        fig.update_layout(
            title="Competitive Positioning Matrix",
            xaxis_title="Specialization (Generalist ← → Specialist)",
            yaxis_title="User Type (Individual ← → Team)",
            xaxis=dict(range=[0, 10], showgrid=True, dtick=1),
            yaxis=dict(range=[0, 10], showgrid=True, dtick=1),
            height=600,
            hovermode='closest',
            showlegend=True,
            # Legend settings removed to restore default position (Right Side)
            font=dict(family=CHART_STYLE['font_family'])
        )
        
        return fig
    
    def plot_feature_comparison(self, features_matrix: pd.DataFrame) -> go.Figure:
        """
        Create radar chart comparing features
        """
        print("🔧 Creating feature comparison chart...")
        
        # Pivot to get scores by competitor
        feature_pivot = features_matrix.pivot(
            index='feature',
            columns='competitor_id',
            values='score'
        )
        
        # Select top competitors to compare
        competitors_to_compare = ['our_product', 'notion_ai', 'mem_ai', 'obsidian']
        
        fig = go.Figure()
        
        colors_map = {
            'our_product': self.colors['accent'],
            'notion_ai': self.colors['primary'],
            'mem_ai': self.colors['secondary'],
            'obsidian': self.colors['info']
        }
        
        for comp_id in competitors_to_compare:
            if comp_id in feature_pivot.columns:
                fig.add_trace(go.Scatterpolar(
                    r=feature_pivot[comp_id],
                    theta=feature_pivot.index,
                    fill='toself',
                    name=comp_id.replace('_', ' ').title(),
                    line_color=colors_map.get(comp_id, self.colors['primary'])
                ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 10])
            ),
            showlegend=True,
            title="Feature Comparison: Our Product vs Top Competitors",
            height=700,
            font=dict(family=CHART_STYLE['font_family'])
        )
        
        return fig
    
    def plot_tam_sam_som_funnel(self, market_data: Dict) -> go.Figure:
        """
        Create funnel visualization for TAM/SAM/SOM
        """
        print("🌍 Creating TAM/SAM/SOM funnel...")
        
        fig = go.Figure(go.Funnel(
            y=['TAM<br>(Total Addressable Market)',
               'SAM<br>(Serviceable Available Market)',
               'SOM<br>(Serviceable Obtainable Market)'],
            x=[market_data['tam']['final'],
               market_data['sam']['final'],
               market_data['som']['final']],
            textposition="inside",
            textinfo="value+percent initial",
            marker=dict(
                color=[self.colors['primary'], self.colors['secondary'], self.colors['accent']]
            ),
            connector=dict(line=dict(color=self.colors['primary'], width=2))
        ))
        
        fig.update_layout(
            title="Market Sizing Funnel (Users)",
            height=500,
            font=dict(family=CHART_STYLE['font_family'])
        )
        
        return fig
    
    def plot_financial_projections(self, projections_df: pd.DataFrame) -> go.Figure:
        """
        Create multi-panel financial projections chart with dedicated legend columns
        Layout: [Graph] [Legend] [SPACER] [Graph] [Legend]
        """
        print("💰 Creating financial projections chart...")
        
        # 5-Column Grid with TIGHT Spacing
        # Col 1 (Graph): 38%
        # Col 2 (Legend): 7%
        # Col 3 (Spacer): 10%
        # Col 4 (Graph): 38%
        # Col 5 (Legend): 7%
        
        fig = make_subplots(
            rows=2, cols=5,
            column_widths=[0.38, 0.07, 0.10, 0.38, 0.07],
            subplot_titles=('User Growth', 'Revenue Growth', 
                          'Unit Economics', 'Profitability'),
            specs=[
                [{'secondary_y': False}, None, None, {'secondary_y': False}, None],
                [{'secondary_y': False}, None, None, {'secondary_y': True}, None]
            ],
            horizontal_spacing=0.01,
            vertical_spacing=0.15
        )
        
        # --- Panel 1: User Growth (Row 1, Col 1) ---
        fig.add_trace(
            go.Scatter(x=projections_df['month'], y=projections_df['total_users'],
                      name='Total Users', line=dict(color=self.colors['primary'], width=2.5),
                      legend="legend"),
            row=1, col=1
        )
        fig.add_trace(
            go.Scatter(x=projections_df['month'], y=projections_df['paying_users'],
                      name='Paying Users', line=dict(color=self.colors['accent'], width=2.5),
                      legend="legend"),
            row=1, col=1
        )
        
        # --- Panel 2: Revenue Growth (Row 1, Col 4) ---
        fig.add_trace(
            go.Scatter(x=projections_df['month'], y=projections_df['mrr'],
                      name='MRR', fill='tozeroy', line=dict(color=self.colors['success']),
                      legend="legend2"),
            row=1, col=4
        )
        
        # --- Panel 3: Unit Economics (Row 2, Col 1) ---
        fig.add_trace(
            go.Scatter(x=projections_df['month'], y=projections_df['ltv_cac_ratio'],
                      name='LTV/CAC Ratio', line=dict(color=self.colors['accent'], width=2.5),
                      legend="legend3"),
            row=2, col=1
        )
        fig.add_hline(y=3.0, line_dash="dash", line_color="green", 
                     annotation_text="Target: 3.0x", row=2, col=1)
        
        # --- Panel 4: Profitability (Row 2, Col 4) ---
        fig.add_trace(
            go.Scatter(x=projections_df['month'], y=projections_df['gross_profit'],
                      name='Gross Profit', line=dict(color=self.colors['success']),
                      legend="legend4"),
            row=2, col=4
        )
        fig.add_trace(
            go.Scatter(x=projections_df['month'], y=projections_df['net_profit'],
                      name='Net Profit', line=dict(color=self.colors['primary']),
                      legend="legend4"),
            row=2, col=4, secondary_y=False
        )
        fig.add_hline(y=0, line_color="red", line_dash="dash", row=2, col=4)
        
        # Update axes titles for Graph Columns (1 and 4)
        for c in [1, 4]:
            fig.update_xaxes(title_text="Month", row=1, col=c)
            fig.update_xaxes(title_text="Month", row=2, col=c)
        
        fig.update_yaxes(title_text="Users", row=1, col=1)
        fig.update_yaxes(title_text="MRR ($)", row=1, col=4)
        fig.update_yaxes(title_text="Ratio", row=2, col=1)
        fig.update_yaxes(title_text="Profit ($)", row=2, col=4)
        
        # --- FIXED LEGEND POSITIONS ---
        # Legend 1/3 (Col 2): x=0.365 (Sticks to Graph 1's right edge)
        # Legend 2/4 (Col 5): x=0.925 (Sticks to Graph 2's right edge - moved from 0.93)
        
        fig.update_layout(
            height=900,
            title_text="24-Month Financial Projections",
            title_font_size=20,
            font=dict(family=CHART_STYLE['font_family']),
            
            # Legend 1
            legend=dict(x=0.365, y=1.0, xanchor='left', yanchor='top', bgcolor='rgba(0,0,0,0)'),
            
            # Legend 2 - Updated to 0.925
            legend2=dict(x=0.925, y=1.0, xanchor='left', yanchor='top', bgcolor='rgba(0,0,0,0)'),
            
            # Legend 3
            legend3=dict(x=0.365, y=0.44, xanchor='left', yanchor='top', bgcolor='rgba(0,0,0,0)'),
            
            # Legend 4 - Updated to 0.925
            legend4=dict(x=0.925, y=0.44, xanchor='left', yanchor='top', bgcolor='rgba(0,0,0,0)'),
        )
        
        return fig
    
    def plot_channel_mix(self, channel_data: Dict) -> go.Figure:
        """
        Create pie chart showing channel mix
        """
        print("📡 Creating channel mix chart...")
        
        channels = channel_data['channels']
        names = [ch['name'] for ch in channels.values()]
        values = [ch['expected_users'] for ch in channels.values()]
        
        fig = go.Figure(data=[go.Pie(
            labels=names,
            values=values,
            hole=0.4,
            marker_colors=[self.colors['primary'], self.colors['secondary'], 
                          self.colors['accent'], self.colors['success'],
                          self.colors['warning'], self.colors['info']]
        )])
        
        fig.update_layout(
            title="User Acquisition Channel Mix",
            height=500,
            font=dict(family=CHART_STYLE['font_family']),
            annotations=[dict(text='Total<br>Users', x=0.5, y=0.5, font_size=20, showarrow=False)]
        )
        
        return fig
    
    def plot_pricing_comparison(self, pricing_data: pd.DataFrame) -> go.Figure:
        """
        Create bar chart comparing pricing
        """
        print("💵 Creating pricing comparison chart...")
        
        # Filter to paid tiers only
        paid_tiers = pricing_data[pricing_data['price_monthly'] > 0].copy()
        
        # Group by competitor, get lowest price
        competitor_prices = paid_tiers.groupby('competitor_name')['price_monthly'].min().reset_index()
        competitor_prices = competitor_prices.sort_values('price_monthly')
        
        # Highlight our product
        colors = [self.colors['accent'] if 'Research' in name else self.colors['primary'] 
                 for name in competitor_prices['competitor_name']]
        
        fig = go.Figure(data=[
            go.Bar(
                y=competitor_prices['competitor_name'],
                x=competitor_prices['price_monthly'],
                orientation='h',
                marker_color=colors,
                text=competitor_prices['price_monthly'].apply(lambda x: f'${x:.0f}/mo'),
                textposition='outside'
            )
        ])
        
        fig.update_layout(
            title="Competitive Pricing Comparison (Lowest Paid Tier)",
            xaxis_title="Price (USD/month)",
            yaxis_title="Product",
            height=500,
            font=dict(family=CHART_STYLE['font_family'])
        )
        
        return fig


if __name__ == "__main__":
    print("=" * 80)
    print(" GTM VISUALIZATION GENERATOR")
    print("=" * 80)
    print()
    
    viz = GTMVisualizer()
    
    # Load data
    try:
        positioning_data = pd.read_csv(PROCESSED_DATA_DIR / 'positioning_data.csv')
        features_matrix = pd.read_csv(PROCESSED_DATA_DIR / 'feature_matrix.csv')
        financial_projections = pd.read_csv(PROCESSED_DATA_DIR / 'financial_projections_24m.csv')
        
        # Create visualizations
        print("\nGenerating visualizations...")
        
        # Positioning matrix
        fig1 = viz.plot_positioning_matrix(positioning_data)
        fig1.write_html(DASHBOARDS_DIR / 'positioning_matrix.html')
        print("✅ Saved: positioning_matrix.html")
        
        # Feature comparison
        fig2 = viz.plot_feature_comparison(features_matrix)
        fig2.write_html(DASHBOARDS_DIR / 'feature_comparison.html')
        print("✅ Saved: feature_comparison.html")
        
        # Financial projections
        fig3 = viz.plot_financial_projections(financial_projections)
        fig3.write_html(DASHBOARDS_DIR / 'financial_projections.html')
        print("✅ Saved: financial_projections.html")
        
        print("\n✅ All visualizations generated successfully!")
        
    except FileNotFoundError as e:
        print(f"⚠️  Data files not found: {e}")
        print("   Run data generation scripts first")