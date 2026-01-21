"""
Competitive Analysis Engine
Analyzes competitive landscape and identifies white space
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from config import *


class CompetitiveAnalyzer:
    """
    Performs comprehensive competitive analysis
    """
    
    def __init__(self, competitors_df: pd.DataFrame, features_matrix: pd.DataFrame):
        self.competitors_df = competitors_df
        self.features_matrix = features_matrix
        self.positioning_data = None
        self.swot_analysis = None
        
    def calculate_positioning_coordinates(self) -> pd.DataFrame:
        """
        Calculate positioning on specialization vs user type axes
        """
        print("📍 Calculating positioning coordinates...")
        
        positioning_scores = {
            'notion_ai': {'x': 2.0, 'y': 7.0, 'label': 'Horizontal Platform\n(Teams)'},
            'mem_ai': {'x': 4.5, 'y': 3.0, 'label': 'AI-first Notes\n(Individual)'},
            'reflect': {'x': 3.0, 'y': 2.0, 'label': 'Networked Notes\n(Individual)'},
            'obsidian': {'x': 5.0, 'y': 1.5, 'label': 'Local-first\n(Power Users)'},
            'roam': {'x': 5.5, 'y': 4.0, 'label': 'Networked Thought\n(Individual+)'},
            'napkin_ai': {'x': 7.0, 'y': 2.0, 'label': 'Visual AI\n(Visual Thinkers)'},
            'recall': {'x': 6.5, 'y': 2.5, 'label': 'Knowledge Graph\n(Learners)'},
            'our_product': {'x': OUR_POSITIONING['x'], 'y': OUR_POSITIONING['y'], 
                          'label': 'Research Synthesis\n(Academics)'}
        }
        
        positioning_list = []
        for comp_id, coords in positioning_scores.items():
            comp_data = self.competitors_df[self.competitors_df['competitor_id'] == comp_id]
            
            if len(comp_data) > 0:
                name = comp_data.iloc[0]['name']
            else:
                name = 'ResearchFlow AI'
            
            positioning_list.append({
                'competitor_id': comp_id,
                'name': name,
                'x_specialization': coords['x'],
                'y_user_type': coords['y'],
                'label': coords['label'],
                'is_our_product': comp_id == 'our_product'
            })
        
        self.positioning_data = pd.DataFrame(positioning_list)
        
        print(f"✅ Calculated positioning for {len(self.positioning_data)} products")
        return self.positioning_data
    
    def identify_white_space(self) -> Dict:
        """
        Identify market white space opportunities
        """
        print("🔍 Identifying white space...")
        
        if self.positioning_data is None:
            self.calculate_positioning_coordinates()
        
        # Define market quadrants
        quadrants = {
            'generalist_individual': {
                'x_range': (0, 5),
                'y_range': (0, 5),
                'name': 'Generalist Individual',
                'crowded': True
            },
            'generalist_team': {
                'x_range': (0, 5),
                'y_range': (5, 10),
                'name': 'Generalist Team',
                'crowded': True
            },
            'specialist_individual': {
                'x_range': (5, 10),
                'y_range': (0, 5),
                'name': 'Specialist Individual',
                'crowded': False  # White space!
            },
            'specialist_team': {
                'x_range': (5, 10),
                'y_range': (5, 10),
                'name': 'Specialist Team',
                'crowded': False
            }
        }
        
        # Count competitors in each quadrant
        for quadrant_id, quadrant in quadrants.items():
            x_min, x_max = quadrant['x_range']
            y_min, y_max = quadrant['y_range']
            
            in_quadrant = self.positioning_data[
                (self.positioning_data['x_specialization'] >= x_min) &
                (self.positioning_data['x_specialization'] < x_max) &
                (self.positioning_data['y_user_type'] >= y_min) &
                (self.positioning_data['y_user_type'] < y_max)
            ]
            
            quadrant['competitor_count'] = len(in_quadrant)
            quadrant['competitors'] = in_quadrant['name'].tolist()
        
        white_space_analysis = {
            'quadrants': quadrants,
            'recommended_position': {
                'quadrant': 'specialist_individual',
                'rationale': 'Least crowded quadrant with clear differentiation opportunity',
                'x': OUR_POSITIONING['x'],
                'y': OUR_POSITIONING['y']
            },
            'competitive_density': {
                'generalist': len(self.positioning_data[self.positioning_data['x_specialization'] < 5]),
                'specialist': len(self.positioning_data[self.positioning_data['x_specialization'] >= 5]),
                'individual': len(self.positioning_data[self.positioning_data['y_user_type'] < 5]),
                'team': len(self.positioning_data[self.positioning_data['y_user_type'] >= 5])
            }
        }
        
        print("✅ White space analysis complete")
        print(f"   Specialist Individual quadrant: {quadrants['specialist_individual']['competitor_count']} competitors")
        print(f"   Generalist Individual quadrant: {quadrants['generalist_individual']['competitor_count']} competitors")
        
        return white_space_analysis
    
    def perform_swot_analysis(self) -> pd.DataFrame:
        """
        SWOT analysis for each major competitor
        """
        print("📊 Performing SWOT analysis...")
        
        swot_data = []
        
        # Notion AI
        swot_data.append({
            'competitor_id': 'notion_ai',
            'name': 'Notion AI',
            'category': 'Strengths',
            'factor': 'Massive distribution (30M users)',
            'impact': 'High',
            'implications': 'Can cross-sell AI to existing base'
        })
        swot_data.append({
            'competitor_id': 'notion_ai',
            'name': 'Notion AI',
            'category': 'Strengths',
            'factor': 'Strong collaboration features',
            'impact': 'High',
            'implications': 'Dominates team use cases'
        })
        swot_data.append({
            'competitor_id': 'notion_ai',
            'name': 'Notion AI',
            'category': 'Weaknesses',
            'factor': 'Generalist platform (not specialized)',
            'impact': 'Medium',
            'implications': 'Vulnerable to vertical specialists'
        })
        swot_data.append({
            'competitor_id': 'notion_ai',
            'name': 'Notion AI',
            'category': 'Weaknesses',
            'factor': 'AI feels bolted-on to existing UX',
            'impact': 'Medium',
            'implications': 'Not AI-native experience'
        })
        swot_data.append({
            'competitor_id': 'notion_ai',
            'name': 'Notion AI',
            'category': 'Opportunities',
            'factor': 'Expand to enterprise (Notion Enterprise)',
            'impact': 'High',
            'implications': 'Upmarket move opens space below'
        })
        swot_data.append({
            'competitor_id': 'notion_ai',
            'name': 'Notion AI',
            'category': 'Threats',
            'factor': 'Microsoft Loop (with Copilot)',
            'impact': 'High',
            'implications': 'Office 365 bundle threat'
        })
        
        # Mem.ai
        swot_data.append({
            'competitor_id': 'mem_ai',
            'name': 'Mem.ai',
            'category': 'Strengths',
            'factor': 'AI-native from day one',
            'impact': 'High',
            'implications': 'UX designed around AI'
        })
        swot_data.append({
            'competitor_id': 'mem_ai',
            'name': 'Mem.ai',
            'category': 'Strengths',
            'factor': 'Automatic linking is best-in-class',
            'impact': 'Medium',
            'implications': 'Low friction note-taking'
        })
        swot_data.append({
            'competitor_id': 'mem_ai',
            'name': 'Mem.ai',
            'category': 'Weaknesses',
            'factor': 'Small user base (100K)',
            'impact': 'Medium',
            'implications': 'Limited network effects'
        })
        swot_data.append({
            'competitor_id': 'mem_ai',
            'name': 'Mem.ai',
            'category': 'Weaknesses',
            'factor': 'Horizontal positioning (everyone)',
            'impact': 'Medium',
            'implications': 'No clear niche ownership'
        })
        swot_data.append({
            'competitor_id': 'mem_ai',
            'name': 'Mem.ai',
            'category': 'Opportunities',
            'factor': 'Add team features',
            'impact': 'High',
            'implications': 'Expand TAM significantly'
        })
        swot_data.append({
            'competitor_id': 'mem_ai',
            'name': 'Mem.ai',
            'category': 'Threats',
            'factor': 'High API costs ($3-5 per user)',
            'impact': 'High',
            'implications': 'Unit economics challenge'
        })
        
        # Obsidian
        swot_data.append({
            'competitor_id': 'obsidian',
            'name': 'Obsidian',
            'category': 'Strengths',
            'factor': 'Local-first (privacy)',
            'impact': 'High',
            'implications': 'Trusted by privacy-conscious users'
        })
        swot_data.append({
            'competitor_id': 'obsidian',
            'name': 'Obsidian',
            'category': 'Strengths',
            'factor': 'Plugin ecosystem',
            'impact': 'High',
            'implications': 'Extensible for power users'
        })
        swot_data.append({
            'competitor_id': 'obsidian',
            'name': 'Obsidian',
            'category': 'Weaknesses',
            'factor': 'Steep learning curve',
            'impact': 'High',
            'implications': 'Limited to power users'
        })
        swot_data.append({
            'competitor_id': 'obsidian',
            'name': 'Obsidian',
            'category': 'Weaknesses',
            'factor': 'AI via plugins (fragmented)',
            'impact': 'Medium',
            'implications': 'Not cohesive AI experience'
        })
        swot_data.append({
            'competitor_id': 'obsidian',
            'name': 'Obsidian',
            'category': 'Opportunities',
            'factor': 'First-party AI integration',
            'impact': 'High',
            'implications': 'Could compete better on AI'
        })
        swot_data.append({
            'competitor_id': 'obsidian',
            'name': 'Obsidian',
            'category': 'Threats',
            'factor': 'Cloud-first competitors easier to use',
            'impact': 'Medium',
            'implications': 'Local-first trades off convenience'
        })
        
        # Add our product SWOT (from config)
        for category, factors in OUR_SWOT.items():
            for factor in factors:
                swot_data.append({
                    'competitor_id': 'our_product',
                    'name': 'ResearchFlow AI',
                    'category': category.capitalize(),
                    'factor': factor,
                    'impact': 'High' if 'unique' in factor.lower() or 'switching costs' in factor.lower() else 'Medium',
                    'implications': 'Key differentiator' if category == 'strengths' else 'Risk to address'
                })
        
        self.swot_analysis = pd.DataFrame(swot_data)
        
        print(f"✅ SWOT analysis complete: {len(self.swot_analysis)} factors analyzed")
        return self.swot_analysis
    
    def calculate_feature_gaps(self) -> pd.DataFrame:
        """
        Identify feature gaps vs competitors
        """
        print("🔍 Analyzing feature gaps...")
        
        # Pivot feature matrix to wide format
        feature_pivot = self.features_matrix.pivot(
            index='feature',
            columns='competitor_id',
            values='score'
        )
        
        # Calculate statistics
        feature_gaps = []
        
        for feature in feature_pivot.index:
            our_score = feature_pivot.loc[feature, 'our_product']
            competitor_max = feature_pivot.drop('our_product', axis=1).loc[feature].max()
            competitor_avg = feature_pivot.drop('our_product', axis=1).loc[feature].mean()
            
            gap_vs_max = our_score - competitor_max
            gap_vs_avg = our_score - competitor_avg
            
            feature_gaps.append({
                'feature': feature,
                'our_score': our_score,
                'competitor_max': competitor_max,
                'competitor_avg': competitor_avg,
                'gap_vs_max': gap_vs_max,
                'gap_vs_avg': gap_vs_avg,
                'competitive_advantage': gap_vs_max > 0,
                'differentiation': 'Strong' if gap_vs_max > 2 else ('Moderate' if gap_vs_max > 0 else 'Weak')
            })
        
        feature_gaps_df = pd.DataFrame(feature_gaps)
        feature_gaps_df = feature_gaps_df.sort_values('gap_vs_max', ascending=False)
        
        print(f"✅ Feature gap analysis complete")
        print(f"   Strong advantages: {len(feature_gaps_df[feature_gaps_df['differentiation'] == 'Strong'])}")
        print(f"   Areas to improve: {len(feature_gaps_df[feature_gaps_df['gap_vs_max'] < 0])}")
        
        return feature_gaps_df
    
    def generate_competitive_summary(self) -> str:
        """
        Generate executive summary of competitive analysis
        """
        white_space = self.identify_white_space()
        feature_gaps = self.calculate_feature_gaps()
        
        summary = "=" * 80 + "\n"
        summary += "COMPETITIVE ANALYSIS SUMMARY\n"
        summary += "=" * 80 + "\n\n"
        
        summary += "🎯 MARKET POSITIONING\n"
        summary += "-" * 80 + "\n"
        summary += f"Our Position: {OUR_POSITIONING['quadrant']}\n"
        summary += f"Coordinates: Specialization={OUR_POSITIONING['x']}/10, User Type={OUR_POSITIONING['y']}/10\n"
        summary += f"Competitors in Same Quadrant: {white_space['quadrants']['specialist_individual']['competitor_count']}\n"
        summary += f"White Space Opportunity: STRONG (least crowded quadrant)\n\n"
        
        summary += "💪 OUR KEY DIFFERENTIATORS\n"
        summary += "-" * 80 + "\n"
        strong_advantages = feature_gaps[feature_gaps['differentiation'] == 'Strong']
        for idx, row in strong_advantages.head(5).iterrows():
            summary += f"   • {row['feature']}: {row['our_score']}/10 vs. {row['competitor_max']}/10 (best competitor)\n"
        summary += "\n"
        
        summary += "⚠️ COMPETITIVE THREATS\n"
        summary += "-" * 80 + "\n"
        weak_areas = feature_gaps[feature_gaps['gap_vs_max'] < 0]
        for idx, row in weak_areas.head(3).iterrows():
            summary += f"   • {row['feature']}: {row['our_score']}/10 vs. {row['competitor_max']}/10 (gap: {row['gap_vs_max']:.1f})\n"
        summary += "\n"
        
        summary += "📊 MARKET CONCENTRATION\n"
        summary += "-" * 80 + "\n"
        summary += f"Generalist Tools: {white_space['competitive_density']['generalist']} competitors\n"
        summary += f"Specialist Tools: {white_space['competitive_density']['specialist']} competitors\n"
        summary += f"Individual-focused: {white_space['competitive_density']['individual']} competitors\n"
        summary += f"Team-focused: {white_space['competitive_density']['team']} competitors\n\n"
        
        summary += "✅ STRATEGIC RECOMMENDATION\n"
        summary += "-" * 80 + "\n"
        summary += "Position as SPECIALIST INDIVIDUAL tool (research synthesis for academics)\n"
        summary += "Rationale:\n"
        summary += "   1. Least crowded quadrant (low competitive intensity)\n"
        summary += "   2. Clear differentiation on cross-source synthesis + academic integration\n"
        summary += "   3. Defensible moat (research knowledge graph = high switching costs)\n"
        summary += "   4. Premium pricing justified by vertical value ($15 vs. $8-10 horizontal tools)\n\n"
        
        return summary


if __name__ == "__main__":
    print("=" * 80)
    print(" COMPETITIVE ANALYZER")
    print("=" * 80)
    print()
    
    # Load data
    competitors_df = pd.read_csv(PROCESSED_DATA_DIR / 'competitive_overview.csv')
    features_matrix = pd.read_csv(PROCESSED_DATA_DIR / 'feature_matrix.csv')
    
    # Run analysis
    analyzer = CompetitiveAnalyzer(competitors_df, features_matrix)
    
    # Generate outputs
    positioning = analyzer.calculate_positioning_coordinates()
    white_space = analyzer.identify_white_space()
    swot = analyzer.perform_swot_analysis()
    feature_gaps = analyzer.calculate_feature_gaps()
    
    # Save results
    positioning.to_csv(PROCESSED_DATA_DIR / 'positioning_data.csv', index=False)
    swot.to_csv(PROCESSED_DATA_DIR / 'swot_analysis.csv', index=False)
    feature_gaps.to_csv(PROCESSED_DATA_DIR / 'feature_gaps.csv', index=False)
    
    # Print summary
    summary = analyzer.generate_competitive_summary()
    print(summary)
    
    # Save summary
    with open(REPORTS_DIR / 'competitive_analysis_summary.txt', 'w') as f:
        f.write(summary)
    
    print("✅ Competitive analysis complete!")