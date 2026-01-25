"""
Streamlit Dashboard for GTM Strategy
Interactive presentation of go-to-market analysis
"""

from streamlit_option_menu import option_menu
from datetime import datetime
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import sys
import textwrap

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from config import *
from visualization import GTMVisualizer

# Page configuration
st.set_page_config(
    page_title="GTM Strategy: AI Research Assistant",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown(
    """
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #6366f1;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 2.2rem;       /* Increased size (was 1.5rem) */
        font-weight: 700;        /* Make it BOLD */
        color: #8b5cf6;          /* Keep the purple brand color */
        margin-top: 3.5rem;      /* More space above to separate sections */
        margin-bottom: 1.5rem;   /* Space below the header */
        border-bottom: 2px solid #8b5cf6; /* Add a line under the header */
        padding-bottom: 10px;    /* Space between text and line */
        letter-spacing: -0.5px;  /* Tighter, more modern look */
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    /* UPDATED: Added specific color rules for text visibility */
    .insight-box {
        background-color: #f0f9ff;
        border-left: 4px solid #3b82f6;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 4px;
        color: #1f2937 !important; /* Force dark text */
    }
    /* Force headings and list items inside the box to be dark too */
    .insight-box h3, .insight-box p, .insight-box li, .insight-box strong {
        color: #1f2937 !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# Initialize visualizer
@st.cache_resource
def get_visualizer():
    return GTMVisualizer()


viz = get_visualizer()


# Load data
@st.cache_data
def load_data():
    data = {}
    try:
        data["competitors"] = pd.read_csv(
            PROCESSED_DATA_DIR / "competitive_overview.csv"
        )
        data["features"] = pd.read_csv(PROCESSED_DATA_DIR / "feature_matrix.csv")
        data["positioning"] = pd.read_csv(PROCESSED_DATA_DIR / "positioning_data.csv")
        data["swot"] = pd.read_csv(PROCESSED_DATA_DIR / "swot_analysis.csv")
        data["financial"] = pd.read_csv(
            PROCESSED_DATA_DIR / "financial_projections_24m.csv"
        )
        data["gtm_plan"] = pd.read_csv(PROCESSED_DATA_DIR / "gtm_weekly_plan.csv")
    except FileNotFoundError:
        st.error("⚠️ Data files not found. Please run data generation scripts first.")
        st.stop()
    return data


data = load_data()

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("### 🚀 GTM Strategy")

    # Clean navigation with icons
    selected_page = option_menu(
        menu_title=None,  # Hidden title
        options=[
            "Executive Summary",
            "Market Opportunity",
            "Competitive Analysis",
            "Pricing Strategy",
            "90-Day GTM Plan",
            "Financial Projections",
            "Dashboard",
        ],
        icons=[
            "house",  # Executive Summary
            "bullseye",  # Market Opportunity
            "trophy",  # Competitive Analysis
            "tag",  # Pricing Strategy
            "calendar-check",  # GTM Plan
            "graph-up-arrow",  # Financials
            "speedometer2",  # Dashboard
        ],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#8b5cf6", "font-size": "16px"},
            "nav-link": {
                "font-size": "14px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#f0f2f6",
            },
            "nav-link-selected": {
                "background-color": "#6366f1",
                "color": "white",
                "font-weight": "500",
            },
        },
    )

    st.markdown("")

    # Styled Product Overview with Floating & Shadow Effect
    st.markdown(
        f"""
        <style>
            .product-card {{
                background-color: #f8f9fa;
                padding: 20px;
                border-radius: 12px;
                border: 1px solid #e5e7eb;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                margin-bottom: 20px;
            }}
            .product-card:hover {{
                transform: translateY(-5px);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            }}
            .product-card p {{
                margin: 0;
            }}
        </style>

        <div class="product-card">
            <p style="font-size: 15px; font-weight: 700; color: #111827; margin-bottom: 8px;">
                {PRODUCT_NAME}
            </p>
            <p style="font-size: 12px; font-style: italic; color: #6b7280; margin-bottom: 12px;">
                {PRODUCT_TAGLINE}
            </p>
            <p style="font-size: 11px; color: #4b5563; line-height: 1.5;">
                An AI-powered research synthesis tool that helps researchers build knowledge graphs and find insights faster.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown("")

# --- SIDEBAR FOOTER ---
st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    <div style='text-align: center; font-size: 12px; color: #6b7280;'>
        © 2026 <strong>Ayush Saxena</strong>. <br>All rights reserved.
    </div>
    """,
    unsafe_allow_html=True,
)

# Main content based on selected page
if selected_page == "Executive Summary":
    st.markdown(
        '<h1 class="main-header">🚀 Go-to-Market Strategy</h1>', unsafe_allow_html=True
    )
    st.markdown(
        f'<h2 style="text-align: center; color: #6366f1;">{PRODUCT_NAME}</h2>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<h3 style="text-align: center; color: #8b5cf6; font-style: italic;">{PRODUCT_TAGLINE}</h3>',
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Key metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <div class="metric-card">
                <h2>$36M</h2>
                <p>ARR Potential</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="metric-card">
                <h2>2M</h2>
                <p>Target Market (SOM)</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="metric-card">
                <h2>7.2x</h2>
                <p>LTV/CAC Ratio</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            """
            <div class="metric-card">
                <h2>3.3 mo</h2>
                <p>CAC Payback</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Problem Statement
    st.markdown(
        '<p class="sub-header">📋 Problem Statement</p>', unsafe_allow_html=True
    )
    st.markdown("""
    Knowledge workers (academic researchers, PhD students, consultants, journalists) struggle to 
    synthesize information from multiple sources. They collect hundreds of articles, papers, and notes 
    but lack tools to connect insights across sources and resurface relevant knowledge when needed.
    
    **Market Inefficiency:** Existing AI productivity tools either:
    - Add AI to existing workflows without redesigning UX (incremental, not transformative)
    - Target everyone, failing to solve specific workflows deeply (horizontal, not vertical)
    - Focus on individual note-taking rather than research synthesis (features, not jobs-to-be-done)
    """)

    # Opportunity
    st.markdown("")
    st.markdown('<p class="sub-header">💡 The Opportunity</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **Market Gap:**
        - 7 major competitors, all horizontal platforms
        - No vertical specialist for research synthesis
        - Specialist Individual quadrant = WHITE SPACE
        
        **Our Positioning:**
        - Deep focus on academic researchers (beachhead)
        - Cross-source synthesis (unique value)
        - Academic database integration
        - Research knowledge graph (switching costs)
        """)

    with col2:
        st.markdown("""
        **Business Model:**
        - Freemium: 50 documents free
        - Pro: $15/month (individual researchers)
        - Team: $30/user/month (research labs)
        
        **Unit Economics:**
        - LTV: $252 (24-month retention)
        - CAC: $35 (blended across channels)
        - Payback: 3.3 months
        - Gross Margin: 70%
        """)

    # Strategic Insight
    st.markdown(
        """
    <div class="insight-box">
        <h3>🎯 Strategic Insight</h3>
        <p><strong>Why we'll win:</strong> While competitors compete on "better AI summarization" 
        (commoditized), we compete on "research synthesis workflow" (defensible). Our knowledge graph 
        compounds switching costs over time, creating a moat that general-purpose tools can't replicate.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # 90-Day Plan Summary
    st.markdown("")
    st.markdown(
        '<p class="sub-header">📅 90-Day Launch Plan</p>', unsafe_allow_html=True
    )

    tab1, tab2, tab3 = st.tabs(
        [
            "Phase 1: Beta (Days 1-30)",
            "Phase 2: Launch (Days 31-60)",
            "Phase 3: Scale (Days 61-90)",
        ]
    )

    with tab1:
        st.markdown("""
        **Goals:**
        - Recruit 100 beta users (academic researchers)
        - Achieve 40% Day-7 activation
        - Validate product-market fit
        - NPS > 40
        
        **Tactics:**
        - Academic Twitter, Reddit (r/PhD, r/GradSchool)
        - Partner with 3 university research labs
        - Daily user interviews
        - Rapid iteration (2 updates/week)
        
        **Budget:** $5,000
        """)

    with tab2:
        st.markdown("""
        **Goals:**
        - Product Hunt #1 Product of the Day
        - 1,000 sign-ups in first week
        - Establish SEO foundation
        - Build early case studies
        
        **Tactics:**
        - Product Hunt launch (Tuesday 8am PST)
        - 10 SEO articles ("AI research tools")
        - Partnerships: ResearchGate, Academia.edu
        - Reddit AMAs
        
        **Budget:** $15,000
        """)

    with tab3:
        st.markdown("""
        **Goals:**
        - 5,000 total users
        - 10% free-to-paid conversion
        - CAC < $50
        - $7,500 MRR
        
        **Tactics:**
        - Google Ads ($200-400/day budget)
        - Referral program (1 month free)
        - Influencer partnerships (academic YouTubers)
        - Conference presence
        
        **Budget:** $30,000
        """)

elif selected_page == "Market Opportunity":
    st.markdown(
        '<h1 class="main-header">🎯 Market Opportunity</h1>', unsafe_allow_html=True
    )

    # TAM/SAM/SOM
    st.markdown(
        '<p class="sub-header">📊 Market Sizing (TAM/SAM/SOM)</p>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        # Create funnel data
        market_data = {
            "tam": {"final": MARKET_SIZE["tam"]["size"]},
            "sam": {"final": MARKET_SIZE["sam"]["size"]},
            "som": {"final": MARKET_SIZE["som"]["size"]},
        }

        fig = viz.plot_tam_sam_som_funnel(market_data)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown(f"""
        **TAM (Total Addressable Market)**
        - {MARKET_SIZE['tam']['size']:,} global knowledge workers
        - Source: {MARKET_SIZE['tam']['source']}
        
        **SAM (Serviceable Available Market)**
        - {MARKET_SIZE['sam']['size']:,} using AI productivity tools
        - {MARKET_SIZE['sam']['penetration']*100:.1f}% of TAM
        - Source: {MARKET_SIZE['sam']['source']}
        
        **SOM (Serviceable Obtainable Market)**
        - {MARKET_SIZE['som']['size']:,} academic researchers (beachhead)
        - {MARKET_SIZE['som']['penetration']*100:.1f}% of SAM
        - Source: {MARKET_SIZE['som']['source']}
        
        ---
        
        **Revenue Potential @ 10% Conversion:**
        - {int(MARKET_SIZE['som']['size'] * 0.10):,} paying customers
        - ${int(MARKET_SIZE['som']['size'] * 0.10 * 15):,} MRR
        - **${int(MARKET_SIZE['som']['size'] * 0.10 * 15 * 12 / 1_000_000)}M ARR**
        """)

    st.markdown("---")

    # Target Segments
    st.markdown('<p class="sub-header">🎯 Target Segments</p>', unsafe_allow_html=True)

    segments_df = pd.DataFrame(
        [
            {
                "Segment": "Academic Researchers (Primary)",
                "Size": "2M globally",
                "Pain": "Literature reviews take 100+ hours",
                "Value Prop": "Complete reviews 60% faster",
                "Willingness to Pay": "High ($15/month)",
            },
            {
                "Segment": "Management Consultants",
                "Size": "1.5M globally",
                "Pain": "Client research scattered across sources",
                "Value Prop": "Synthesize industry research instantly",
                "Willingness to Pay": "Very High ($30/month)",
            },
            {
                "Segment": "Investigative Journalists",
                "Size": "500K globally",
                "Pain": "Tracking stories across many sources",
                "Value Prop": "Connect dots across documents",
                "Willingness to Pay": "Medium ($12/month)",
            },
        ]
    )

    segments_df.index = segments_df.index + 1

    st.dataframe(segments_df, use_container_width=True, hide_index=True)

    st.markdown(
        """
    <div class="insight-box">
        <h3>📌 Beachhead Strategy</h3>
        <p><strong>Why start with academics?</strong></p>
        <ul>
            <li><strong>Clear workflow:</strong> Literature review → synthesis → writing (predictable)</li>
            <li><strong>High pain:</strong> Spend 100+ hours on lit reviews (quantifiable)</li>
            <li><strong>Network effects:</strong> Researchers cite each other (viral potential)</li>
            <li><strong>Referenceable:</strong> Published papers become case studies (credibility)</li>
            <li><strong>Budget access:</strong> University research grants (less price sensitive)</li>
        </ul>
        <p><strong>Expansion path:</strong> Academics → Consultants → Journalists → Corporate researchers</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

elif selected_page == "Competitive Analysis":
    st.markdown(
        '<h1 class="main-header">🏆 Competitive Analysis</h1>', unsafe_allow_html=True
    )

    # Positioning Matrix
    st.markdown(
        '<p class="sub-header">📍 Competitive Positioning</p>', unsafe_allow_html=True
    )

    fig = viz.plot_positioning_matrix(data["positioning"])
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
    <div class="insight-box">
        <h3>💡 White Space Opportunity</h3>
        <p>The <strong>Specialist Individual</strong> quadrant (bottom-right) has only 2 competitors 
        (Napkin.ai, Recall) vs. 5 in the Generalist Individual quadrant. This is where we position 
        ResearchFlow AI.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Feature Comparison
    st.markdown(
        '<p class="sub-header">🔧 Feature Comparison</p>', unsafe_allow_html=True
    )

    fig = viz.plot_feature_comparison(data["features"])
    st.plotly_chart(fig, use_container_width=True)

    # Competitor Overview
    st.markdown(
        '<p class="sub-header">📊 Competitor Overview</p>', unsafe_allow_html=True
    )

    comp_display = data["competitors"][
        [
            "name",
            "positioning",
            "estimated_users",
            "pricing_lowest",
            "total_funding_usd",
        ]
    ].copy()
    comp_display.columns = ["Product", "Positioning", "Users", "Min Price", "Funding"]
    comp_display["Users"] = comp_display["Users"].apply(lambda x: f"{x:,}")
    comp_display["Min Price"] = comp_display["Min Price"].apply(lambda x: f"${x}/mo")
    comp_display["Funding"] = comp_display["Funding"].apply(
        lambda x: f"${x/1_000_000:.1f}M" if x > 0 else "Bootstrapped"
    )

    comp_display.index = comp_display.index + 1

    st.dataframe(comp_display, use_container_width=True, hide_index=True)

    #    st.markdown("---")

    # SWOT Analysis
    st.markdown("")
    st.markdown("")
    st.markdown(
        '<p class="sub-header">💪 SWOT Analysis (Our Product)</p>',
        unsafe_allow_html=True,
    )

    our_swot = data["swot"][data["swot"]["competitor_id"] == "our_product"]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Strengths:**")
        strengths = our_swot[our_swot["category"] == "Strengths"]["factor"].tolist()
        for s in strengths:
            st.markdown(f"✅ {s}")

        st.markdown("")
        st.markdown("")
        st.markdown("\n**Opportunities:**")
        opportunities = our_swot[our_swot["category"] == "Opportunities"][
            "factor"
        ].tolist()
        for o in opportunities:
            st.markdown(f"🌟 {o}")

    with col2:
        st.markdown("**Weaknesses:**")
        weaknesses = our_swot[our_swot["category"] == "Weaknesses"]["factor"].tolist()
        for w in weaknesses:
            st.markdown(f"⚠️ {w}")

        st.markdown("")
        st.markdown("")
        st.markdown("\n**Threats:**")
        threats = our_swot[our_swot["category"] == "Threats"]["factor"].tolist()
        for t in threats:
            st.markdown(f"⚡ {t}")

elif selected_page == "Pricing Strategy":
    st.markdown(
        '<h1 class="main-header">💰 Pricing Strategy</h1>', unsafe_allow_html=True
    )

    # Proposed Pricing
    st.markdown(
        '<p class="sub-header">💵 Proposed Pricing Tiers</p>', unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### FREE
        **$0/month**
        
        Perfect for trying out
        
        ✅ 50 documents maximum  
        ✅ Basic AI summarization  
        ✅ Manual linking only  
        ✅ Limited knowledge graph  
        ✅ Individual use only  
        &nbsp;
        
        ---
        **Target:** Students, explorers
        """)

    with col2:
        st.markdown("""
        ### PRO ⭐
        **$15/month**
        
        Most popular choice
        
        ✅ Unlimited documents  
        ✅ Cross-source synthesis  
        ✅ Automatic linking  
        ✅ Academic integration  
        ✅ Citation export  
        ✅ Priority support  
        
        ---
        **Target:** PhD students, researchers  
        **Save 20%:** $144/year
        """)

    with col3:
        st.markdown("""
        ### TEAM
        **$30/user/month**
        
        For research teams
        
        ✅ Everything in Pro  
        ✅ Shared knowledge bases  
        ✅ Collaborative synthesis  
        ✅ Team permissions  
        ✅ Admin dashboard  
        ✅ API access  
        
        ---
        **Target:** Research labs  
        **Save 20%:** $288/year
        """)

    st.markdown("---")

    # Competitive Pricing
    st.markdown(
        '<p class="sub-header">📊 Competitive Pricing Landscape</p>',
        unsafe_allow_html=True,
    )

    # Create pricing comparison data
    pricing_comp = pd.DataFrame(
        [
            {
                "Product": "Our Product (Pro)",
                "Price": 15,
                "Positioning": "Specialist",
                "Highlight": True,
            },
            {
                "Product": "Notion AI",
                "Price": 10,
                "Positioning": "Generalist",
                "Highlight": False,
            },
            {
                "Product": "Mem.ai",
                "Price": 8,
                "Positioning": "Generalist",
                "Highlight": False,
            },
            {
                "Product": "Reflect",
                "Price": 10,
                "Positioning": "Generalist",
                "Highlight": False,
            },
            {
                "Product": "Roam Research",
                "Price": 15,
                "Positioning": "Generalist",
                "Highlight": False,
            },
            {
                "Product": "Recall",
                "Price": 7,
                "Positioning": "Specialist",
                "Highlight": False,
            },
        ]
    )

    fig = go.Figure()

    for _, row in pricing_comp.iterrows():
        color = COLOR_SCHEME["accent"] if row["Highlight"] else COLOR_SCHEME["primary"]
        fig.add_trace(
            go.Bar(
                y=[row["Product"]],
                x=[row["Price"]],
                orientation="h",
                marker_color=color,
                text=f"${row['Price']}/mo",
                textposition="outside",
                name=row["Product"],
                showlegend=False,
            )
        )

    fig.update_layout(
        title="Competitive Pricing Comparison",
        xaxis_title="Monthly Price (USD)",
        height=400,
        font=dict(family=CHART_STYLE["font_family"]),
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Pricing Positioning:**
    - **25% premium** vs. average generalist tool ($12)
    - **Justified by vertical value:** Save $1,875/month in researcher time
    - **ROI:** $15 cost → $1,875 value = **125x ROI**
    """)

    #    st.markdown("---")

    st.markdown("")
    st.markdown(
        """
    <div class="insight-box">
        <h3>🌏 Regional Pricing Strategy (India)</h3>
        <p><strong>Purchasing Power Parity (PPP) Adjustment:</strong></p>
        <p>To capture the large Indian academic market, we will offer a localized price of 
        <strong>₹499/month</strong> (vs $15 global). This lowers the barrier to entry while 
        building a massive user base in our beachhead segment.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Unit Economics
    st.markdown("")
    st.markdown("")
    st.markdown('<p class="sub-header">🧮 Unit Economics</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Customer Acquisition Cost (CAC)", "$35", delta="Blended across channels"
        )
        st.markdown("**Breakdown:**")
        st.markdown("- Product Hunt: $20")
        st.markdown("- SEO/Content: $15")
        st.markdown("- Google Ads: $50")
        st.markdown("- Referrals: $10")

    with col2:
        st.metric("Lifetime Value (LTV)", "$252", delta="24-month retention")
        st.markdown("**Calculation:**")
        st.markdown("- ARPU: $15/month")
        st.markdown("- Lifetime: 24 months")
        st.markdown("- Gross Margin: 70%")
        st.markdown("- LTV = $15 × 24 × 0.70")

    with col3:
        st.metric("LTV/CAC Ratio", "7.2x", delta="Target: > 3.0x")
        st.metric(
            "Payback Period",
            "3.3 months",
            delta="-8.7mo vs target",
            delta_color="inverse",
        )
        st.metric("Gross Margin", "70%", delta="After API costs")

    st.markdown(
        """
    <div class="insight-box">
        <h3>💡 Why Unit Economics Work</h3>
        <ul>
            <li><strong>High LTV:</strong> Research knowledge graph creates switching costs</li>
            <li><strong>Low CAC:</strong> Beachhead strategy enables organic/viral growth</li>
            <li><strong>70% Margin:</strong> API costs declining (GPT-4 → GPT-4-turbo → future models)</li>
            <li><strong>Fast Payback:</strong> SaaS cash flow positive quickly</li>
        </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

elif selected_page == "90-Day GTM Plan":
    st.markdown(
        '<h1 class="main-header">📅 90-Day GTM Plan</h1>', unsafe_allow_html=True
    )

    # Week-by-week view
    st.markdown('<p class="sub-header">📆 Weekly Roadmap</p>', unsafe_allow_html=True)

    # Phase selector
    phase_filter = st.selectbox(
        "Filter by Phase:",
        [
            "All Phases",
            "Phase 1: Private Beta",
            "Phase 2: Public Launch",
            "Phase 3: Paid Acquisition",
        ],
    )

    if phase_filter == "All Phases":
        filtered_plan = data["gtm_plan"]
    else:
        filtered_plan = data["gtm_plan"][data["gtm_plan"]["phase"] == phase_filter]

    # Display as expandable cards
    for _, week in filtered_plan.iterrows():
        with st.expander(
            f"**Week {week['week']}: {week['focus']}** ({week['start_date']} to {week['end_date']})"
        ):
            col1, col2 = st.columns([2, 1])

            with col1:
                st.markdown(f"**Phase:** {week['phase']}")
                st.markdown(f"**Tasks ({week['num_tasks']}):**")
                tasks = week["tasks"].split("; ")
                for task in tasks:
                    st.markdown(f"- {task}")

            with col2:
                st.metric("Budget", f"${week['budget_usd']:,}")
                st.markdown("**Key Metrics:**")

                raw_metrics = week["key_metrics"]

                # LOGIC: Check if it's a raw dictionary string "{...}" and format it
                if isinstance(raw_metrics, str) and raw_metrics.strip().startswith("{"):
                    try:
                        import ast

                        # Safely convert string to dictionary
                        metrics_dict = ast.literal_eval(raw_metrics)

                        # Loop through and print clean bullet points
                        for key, value in metrics_dict.items():
                            # Clean up the key: "activation_rate" -> "Activation Rate"
                            clean_label = key.replace("_", " ").title()
                            st.markdown(f"- **{clean_label}:** {value}")
                    except:
                        # Fallback if parsing fails
                        st.markdown(raw_metrics, unsafe_allow_html=True)
                else:
                    # If it's normal text or HTML (like in other phases), just render it
                    st.markdown(raw_metrics, unsafe_allow_html=True)

    st.markdown("---")

    # Budget Allocation
    st.markdown(
        '<p class="sub-header">💵 Budget Allocation</p>', unsafe_allow_html=True
    )

    # 1. Define Data
    budget_data = pd.DataFrame(
        [
            {"Phase": "Month 1: Foundation", "Amount": 5000, "Focus": "MVP & Setup"},
            {
                "Phase": "Month 2: Validation",
                "Amount": 15000,
                "Focus": "Paid Ads & Content",
            },
            {"Phase": "Month 3: Scaling", "Amount": 30000, "Focus": "Growth & Sales"},
        ]
    )

    # 2. Create Two Columns (Chart | Details)
    col1, col2 = st.columns([1.5, 1])

    with col1:
        # Create Enhanced Donut Chart
        fig = go.Figure(
            data=[
                go.Pie(
                    labels=budget_data["Phase"],
                    values=budget_data["Amount"],
                    hole=0.5,
                    textinfo="label+percent",
                    textposition="inside",
                    marker=dict(
                        colors=[
                            COLOR_SCHEME["secondary"],
                            COLOR_SCHEME["primary"],
                            COLOR_SCHEME["accent"],
                        ]
                    ),
                    hoverinfo="label+value+percent",
                )
            ]
        )

        fig.update_layout(
            title_text="Budget Distribution by Phase",
            title_x=0.2,
            title_pad=dict(b=60),
            title_y=1.0,
            height=400,
            margin=dict(t=60, b=10, l=10, r=10),
            font=dict(family=CHART_STYLE["font_family"]),
            showlegend=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("### 📝 Spending Breakdown")

        # Create a clean visual list using st.info or markdown
        st.info("""
        **Month 1: Foundation ($5k)**
        - Server Infrastructure setup
        - Initial Content Creation
        - Community Launch events
        """)

        st.info("""
        **Month 2: Validation ($15k)**
        - Google Ads testing
        - Influencer partnerships
        - SEO tooling & backlinks
        """)

        st.info("""
        **Month 3: Scaling ($30k)**
        - Aggressive retargeting
        - Affiliate program launch
        - Sales team commisions
        """)

    # Channel Strategy
    st.markdown(
        '<p class="sub-header">📡 Acquisition Channels</p>', unsafe_allow_html=True
    )

    channels_data = pd.DataFrame(
        [
            {
                "Channel": "Product Hunt",
                "Users": 800,
                "CAC": 20,
                "Budget": 5000,
                "Type": "Launch",
            },
            {
                "Channel": "SEO/Content",
                "Users": 1200,
                "CAC": 15,
                "Budget": 10000,
                "Type": "Organic",
            },
            {
                "Channel": "Google Ads",
                "Users": 1500,
                "CAC": 50,
                "Budget": 25000,
                "Type": "Paid",
            },
            {
                "Channel": "Referrals",
                "Users": 600,
                "CAC": 10,
                "Budget": 3000,
                "Type": "Viral",
            },
            {
                "Channel": "Social Media",
                "Users": 500,
                "CAC": 25,
                "Budget": 8000,
                "Type": "Community",
            },
            {
                "Channel": "Partnerships",
                "Users": 400,
                "CAC": 30,
                "Budget": 4000,
                "Type": "B2B",
            },
        ]
    )

    col1, col2 = st.columns(2)

    with col1:
        fig1 = go.Figure(
            data=[
                go.Pie(
                    labels=channels_data["Channel"],
                    values=channels_data["Users"],
                    # Removed title from inside go.Pie to fix spacing issue
                    textinfo="label+percent",
                    textposition="inside",
                )
            ]
        )
        fig1.update_layout(
            title_text="User Acquisition by Channel",
            title_x=0.2,  # Center the title
            title_y=0.9,  # Move it up slightly for spacing
            height=400,
            font=dict(family=CHART_STYLE["font_family"]),
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = go.Figure(
            data=[
                go.Bar(
                    x=channels_data["Channel"],
                    y=channels_data["CAC"],
                    marker_color=COLOR_SCHEME["primary"],
                    text=channels_data["CAC"].apply(lambda x: f"${x}"),
                    textposition="outside",
                )
            ]
        )

        # Calculate max CAC to set y-axis limit dynamically
        max_cac = channels_data["CAC"].max()

        fig2.update_layout(
            title_text="CAC by Channel",
            title_x=0.5,  # Center the title
            yaxis_title="CAC ($)",
            height=400,
            # Add 20% headroom so labels don't get cut off
            yaxis=dict(range=[0, max_cac * 1.2]),
            font=dict(family=CHART_STYLE["font_family"]),
        )
        st.plotly_chart(fig2, use_container_width=True)

    # UPDATE: Start index at 1 instead of 0
    channels_data.index = channels_data.index + 1

    st.markdown("📋 Channel Performance Metrics:")
    st.dataframe(channels_data, use_container_width=True, hide_index=True)

elif selected_page == "Financial Projections":
    st.markdown(
        '<h1 class="main-header">💵 Financial Projections</h1>', unsafe_allow_html=True
    )

    # Interactive projections
    st.markdown(
        '<p class="sub-header">📈 24-Month Projections</p>', unsafe_allow_html=True
    )

    fig = viz.plot_financial_projections(data["financial"])
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Key milestones
    st.markdown('<p class="sub-header">🎯 Key Milestones</p>', unsafe_allow_html=True)

    # Get data rows
    m3 = data["financial"].iloc[2]
    m6 = data["financial"].iloc[5]
    m12 = data["financial"].iloc[11]
    m24 = data["financial"].iloc[23]

    # Custom Styling for Milestone Cards
    st.markdown(
        """
    <style>
        .milestone-card {
            background-color: #1f2937;
            border: 1px solid #374151;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            height: 100%;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s;
        }
        .milestone-card:hover {
            transform: translateY(-5px);
            border-color: #6366f1;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
        }
        .milestone-header {
            color: #8b5cf6;
            font-size: 1.2rem;
            font-weight: 700;
            margin-bottom: 5px;
        }
        .milestone-sub {
            color: #9ca3af;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 20px;
            border-bottom: 1px solid #374151;
            padding-bottom: 10px;
        }
        .metric-row {
            margin-bottom: 15px;
        }
        .metric-val {
            color: #f3f4f6;
            font-size: 1.5rem;
            font-weight: 700;
        }
        .metric-val.revenue {
            color: #34d399; /* Green for money */
        }
        .metric-lbl {
            color: #9ca3af;
            font-size: 0.8rem;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

    # Helper function to generate HTML card
    def create_milestone_card(month, phase, data):
        # We build the HTML as a single flat string to prevent Markdown code-block errors
        # Do not add indentation to the lines inside the string
        html = f"""
<div class="milestone-card">
<div class="milestone-header">Month {month}</div>
<div class="milestone-sub">{phase}</div>
<div class="metric-row">
<div class="metric-val">{data['total_users']:,.0f}</div>
<div class="metric-lbl">Total Users</div>
</div>
<div class="metric-row">
<div class="metric-val">{data['paying_users']:,.0f}</div>
<div class="metric-lbl">Paying Users</div>
</div>
<div class="metric-row">
<div class="metric-val revenue">${data['mrr']:,.0f}</div>
<div class="metric-lbl">MRR</div>
</div>
<div class="metric-row">
<div class="metric-val revenue">${data['arr']:,.0f}</div>
<div class="metric-lbl">ARR</div>
</div>
</div>
"""
        return html

    # Render columns
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(create_milestone_card(3, "End of GTM", m3), unsafe_allow_html=True)
    with c2:
        st.markdown(
            create_milestone_card(6, "Scaling Phase", m6), unsafe_allow_html=True
        )
    with c3:
        st.markdown(
            create_milestone_card(12, "Year 1 End", m12), unsafe_allow_html=True
        )
    with c4:
        st.markdown(
            create_milestone_card(24, "Year 2 End", m24), unsafe_allow_html=True
        )

    st.markdown("---")

    # Detailed table
    st.markdown(
        '<p class="sub-header">📊 Detailed Projections</p>', unsafe_allow_html=True
    )
    st.markdown(
        "24 Months of financial projections including user growth, revenue, and key metrics:"
    )

    # Select columns to display
    display_cols = [
        "month",
        "date",
        "total_users",
        "paying_users",
        "mrr",
        "arr",
        "free_to_paid_rate",
        "churn_rate",
        "ltv_cac_ratio",
        "net_profit",
    ]

    display_df = data["financial"][display_cols].copy()
    display_df.columns = [
        "Month",
        "Date",
        "Total Users",
        "Paying Users",
        "MRR",
        "ARR",
        "Free→Paid %",
        "Churn %",
        "LTV/CAC",
        "Net Profit",
    ]

    # Format numbers
    display_df["Total Users"] = display_df["Total Users"].apply(lambda x: f"{x:,.0f}")
    display_df["Paying Users"] = display_df["Paying Users"].apply(lambda x: f"{x:,.0f}")
    display_df["MRR"] = display_df["MRR"].apply(lambda x: f"${x:,.0f}")
    display_df["ARR"] = display_df["ARR"].apply(lambda x: f"${x:,.0f}")
    display_df["Free→Paid %"] = display_df["Free→Paid %"].apply(
        lambda x: f"{x*100:.1f}%"
    )
    display_df["Churn %"] = display_df["Churn %"].apply(lambda x: f"{x*100:.1f}%")
    display_df["LTV/CAC"] = display_df["LTV/CAC"].apply(lambda x: f"{x:.1f}x")
    display_df["Net Profit"] = display_df["Net Profit"].apply(lambda x: f"${x:,.0f}")

    display_df.index = display_df.index + 1

    st.dataframe(display_df, use_container_width=True, hide_index=True, height=600)

elif selected_page == "Dashboard":
    st.markdown(
        '<h1 class="main-header">📊 Executive Dashboard</h1>', unsafe_allow_html=True
    )

    # Summary metrics
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "TAM", f"{MARKET_SIZE['tam']['size']/1_000_000:.0f}M", "Knowledge Workers"
        )

    with col2:
        st.metric(
            "SAM",
            f"{MARKET_SIZE['sam']['size']/1_000_000:.0f}M",
            f"{MARKET_SIZE['sam']['penetration']*100:.0f}% of TAM",
        )

    with col3:
        st.metric(
            "SOM",
            f"{MARKET_SIZE['som']['size']/1_000_000:.1f}M",
            f"{MARKET_SIZE['som']['penetration']*100:.0f}% of SAM",
        )

    with col4:
        som_revenue = MARKET_SIZE["som"]["size"] * 0.10 * 15 * 12 / 1_000_000
        st.metric("ARR Potential", f"${som_revenue:.0f}M", "10% conversion")

    with col5:
        st.metric("Competitors", len(COMPETITORS), "Major players")

    #    st.markdown("---")

    # Quick insights
    st.markdown("")
    st.markdown("")
    st.markdown(
        '<p class="sub-header">🎯 Key Strategic Insights</p>', unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **Market Position:**
        - ✅ White space in Specialist Individual quadrant
        - ✅ 2 competitors vs. 5 in generalist space
        - ✅ Clear differentiation on research synthesis
        - ✅ Defensible moat (knowledge graph switching costs)
        
        **Competitive Advantages:**
        - Cross-source synthesis (10/10 vs 4-7 competitors)
        - Academic database integration (10/10 vs 0-4)
        - Citation management (10/10 vs 0-5)
        - Knowledge graph visualization (9/10 vs 3-10)
        """)

    with col2:
        st.markdown("""
        **Business Model Health:**
        - ✅ LTV/CAC: 7.2x (Target: >3.0x)
        - ✅ Payback: 3.3 months (Target: <12mo)
        - ✅ Gross Margin: 70% (Target: >60%)
        - ✅ Premium pricing justified by ROI (125x)
        
        **90-Day Targets:**
        - 5,000 total users
        - 500 paying customers (10% conversion)
        - \$7,500 MRR (\$90K ARR)
        - Break-even: Month 9 projected
        """)

    #    st.markdown("---")

    # Download reports
    st.markdown("")
    st.markdown("")
    st.markdown('<p class="sub-header">📥 Download Reports</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📄 Competitive Analysis Report"):
            st.info("Report generated: competitive_analysis_summary.txt")

    with col2:
        if st.button("📄 Market Sizing Report"):
            st.info("Report generated: market_sizing_report.txt")

    with col3:
        if st.button("📄 Financial Projections"):
            st.info("Report generated: financial_model_report.txt")

# --- FOOTER ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #6b7280; padding: 20px;'>
        <p> 🚀 <strong>Go-to-Market Strategy</strong> - AI-Powered Research Assistant</p>
        <p>Built with Python, Streamlit, Pandas, NumPy, Plotly, Matplotlib & Seaborn <strong>| Last Updated:</strong> {}</p>
        <p>© 2026 <strong>Ayush Saxena</strong>. All rights reserved.</p>
    </div>
""".format(datetime.now().strftime("%d-%b-%Y At %I:%M %p")),
    unsafe_allow_html=True,
)
