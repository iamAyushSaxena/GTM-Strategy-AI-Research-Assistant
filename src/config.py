"""
Configuration file for GTM Strategy Project
Author: Ayush Saxena
Date: January 2026
"""

import os
from pathlib import Path
from datetime import datetime

# ===== PROJECT PATHS =====
PROJECT_ROOT = Path(__file__).parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
SYNTHETIC_DATA_DIR = DATA_DIR / "synthetic"
STRATEGY_DIR = PROJECT_ROOT / "strategy"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUT_DIR / "figures"
REPORTS_DIR = OUTPUT_DIR / "reports"
DASHBOARDS_DIR = OUTPUT_DIR / "dashboards"

# Create directories
for directory in [
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    SYNTHETIC_DATA_DIR,
    STRATEGY_DIR,
    FIGURES_DIR,
    REPORTS_DIR,
    DASHBOARDS_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)

# ===== PRODUCT DEFINITION =====
PRODUCT_NAME = "ResearchFlow AI"
PRODUCT_TAGLINE = "AI Research Assistant for Knowledge Workers"
PRODUCT_DESCRIPTION = """
An AI-powered research synthesis tool that reads, connects, and synthesizes 
information across multiple sources, helping researchers build progressive 
knowledge graphs and focus on insights rather than collection.
"""

# ===== TARGET MARKET =====
TARGET_MARKET = {
    "primary": {
        "segment": "Academic Researchers & PhD Students",
        "size": 2_000_000,  # 2M globally
        "description": "Researchers conducting literature reviews, writing papers, building domain knowledge",
    },
    "secondary": {
        "consultants": {
            "segment": "Management Consultants",
            "size": 1_500_000,
            "description": "Consultants synthesizing industry research for client projects",
        },
        "journalists": {
            "segment": "Investigative Journalists",
            "size": 500_000,
            "description": "Journalists tracking stories across multiple sources",
        },
    },
}

# ===== MARKET SIZING (TAM/SAM/SOM) =====
MARKET_SIZE = {
    "tam": {
        "size": 300_000_000,  # 300M knowledge workers globally
        "description": "All knowledge workers (researchers, consultants, analysts, writers)",
        "source": "World Bank, McKinsey Global Institute 2024",
    },
    "sam": {
        "size": 50_000_000,  # 50M who use AI tools
        "description": "Knowledge workers actively using AI productivity tools",
        "penetration": 0.167,  # 16.7% of TAM
        "source": "Gartner AI Adoption Survey 2025",
    },
    "som": {
        "size": 2_000_000,  # 2M academic/research-focused
        "description": "Academic researchers and PhD students (beachhead market)",
        "penetration": 0.04,  # 4% of SAM
        "source": "NSF, UNESCO Institute for Statistics",
    },
}

# ===== COMPETITORS =====
COMPETITORS = {
    "notion_ai": {
        "name": "Notion AI",
        "description": "All-in-one workspace with AI features",
        "founded": 2016,
        "ai_added": 2023,
        "positioning": "Horizontal - Everyone",
        "pricing": {
            "free": True,
            "plus": 10,  # USD per user/month
            "business": 18,
            "enterprise": "Custom",
        },
        "users_estimate": 30_000_000,
        "funding_total": 343_000_000,  # USD
        "latest_valuation": 10_000_000_000,
    },
    "mem_ai": {
        "name": "Mem.ai",
        "description": "AI-first networked note-taking",
        "founded": 2019,
        "ai_added": 2019,  # AI-native
        "positioning": "Horizontal - Knowledge Workers",
        "pricing": {"free": False, "starter": 8, "pro": 15},
        "users_estimate": 100_000,
        "funding_total": 29_500_000,
        "latest_valuation": 100_000_000,
    },
    "reflect": {
        "name": "Reflect",
        "description": "Networked note-taking with AI",
        "founded": 2021,
        "ai_added": 2023,
        "positioning": "Horizontal - Individuals",
        "pricing": {
            "free": False,
            "monthly": 10,
            "annual": 8,  # per month if paid annually
        },
        "users_estimate": 50_000,
        "funding_total": 11_500_000,
        "latest_valuation": 50_000_000,
    },
    "obsidian": {
        "name": "Obsidian",
        "description": "Local-first knowledge base with plugins",
        "founded": 2020,
        "ai_added": 2023,  # Via plugins
        "positioning": "Horizontal - Power Users",
        "pricing": {
            "free": True,
            "catalyst": 25,  # one-time
            "commercial": 50,  # per user/year
        },
        "users_estimate": 1_000_000,
        "funding_total": 0,  # Bootstrapped
        "latest_valuation": None,
    },
    "roam": {
        "name": "Roam Research",
        "description": "Networked thought tool",
        "founded": 2017,
        "ai_added": 2024,
        "positioning": "Horizontal - Researchers & Thinkers",
        "pricing": {"free": False, "pro": 15, "believer": 8.33},  # $500/5 years
        "users_estimate": 200_000,
        "funding_total": 9_000_000,
        "latest_valuation": 200_000_000,
    },
    "napkin_ai": {
        "name": "Napkin.ai",
        "description": "AI that turns text into visual diagrams",
        "founded": 2023,
        "ai_added": 2023,  # AI-native
        "positioning": "Vertical - Visual Thinkers",
        "pricing": {"free": True, "pro": 10},
        "users_estimate": 30_000,
        "funding_total": 3_000_000,
        "latest_valuation": 15_000_000,
    },
    "recall": {
        "name": "Recall",
        "description": "AI knowledge graph from anything you read",
        "founded": 2023,
        "ai_added": 2023,  # AI-native
        "positioning": "Vertical - Learners",
        "pricing": {"free": True, "plus": 7},
        "users_estimate": 40_000,
        "funding_total": 2_000_000,
        "latest_valuation": 10_000_000,
    },
}

# ===== FEATURE COMPARISON DIMENSIONS =====
FEATURE_DIMENSIONS = [
    "AI Summarization",
    "Cross-source Synthesis",
    "Knowledge Graph Visualization",
    "Automatic Linking",
    "Collaboration",
    "Academic Database Integration",
    "Citation Management",
    "Version History",
    "Mobile App",
    "Offline Mode",
    "API Access",
    "Custom AI Prompts",
    "Export Options",
    "Search Quality",
    "Privacy (Local-first)",
]

# ===== POSITIONING FRAMEWORK =====
POSITIONING_AXES = {
    "x_axis": {
        "name": "Specialization",
        "min": "Generalist (Horizontal)",
        "max": "Specialist (Vertical)",
        "description": "Degree of vertical focus vs horizontal platform",
    },
    "y_axis": {
        "name": "User Type",
        "min": "Individual",
        "max": "Team/Enterprise",
        "description": "Primary user segment targeted",
    },
}

# Our product positioning
OUR_POSITIONING = {
    "x": 8.5,  # Highly specialized (0-10 scale)
    "y": 3.0,  # Individual-focused with light collaboration (0-10 scale)
    "quadrant": "Specialist Individual",
    "rationale": "Deep vertical focus on research synthesis workflow for individual academics",
}

# ===== PRICING STRATEGY =====
PRICING_TIERS = {
    "free": {
        "name": "Free",
        "price_monthly": 0,
        "features": [
            "50 documents maximum",
            "Basic AI summarization",
            "Manual linking only",
            "Limited knowledge graph (50 nodes)",
            "Individual use only",
        ],
        "target_conversion": 0.10,  # 10% free-to-paid
    },
    "pro": {
        "name": "Pro",
        "price_monthly": 15,
        "price_annual": 144,  # $12/month if paid annually
        "features": [
            "Unlimited documents",
            "Advanced cross-source synthesis",
            "Automatic linking & knowledge graph",
            "Academic database integration",
            "Citation export (BibTeX, RIS)",
            "Version history (30 days)",
            "Priority support",
        ],
        "target_segment": "PhD students, early-career researchers",
        "value_prop": "Complete literature review in 60% less time",
    },
    "team": {
        "name": "Team",
        "price_monthly": 30,  # per user
        "price_annual": 288,
        "features": [
            "Everything in Pro",
            "Shared knowledge bases",
            "Collaborative synthesis",
            "Team permissions",
            "Admin dashboard",
            "SSO (Google, Microsoft)",
            "API access",
            "Custom integrations",
        ],
        "target_segment": "Research labs, consulting teams",
        "value_prop": "Shared team intelligence, faster onboarding",
    },
}

# ===== UNIT ECONOMICS =====
UNIT_ECONOMICS = {
    "cac": {
        "target": 50,  # USD - target Customer Acquisition Cost
        "breakdown": {
            "product_hunt": 20,  # $20 per user via PH launch
            "seo_content": 15,  # $15 per user via organic
            "paid_ads": 80,  # $80 per user (Google Ads, high intent)
            "referral": 10,  # $10 per user (existing users refer)
        },
        "blended": 35,  # Blended CAC across channels
    },
    "ltv": {
        "arpu": 15,  # Average Revenue Per User (monthly)
        "retention_months": 24,  # Average customer lifetime
        "gross_margin": 0.70,  # 70% after API costs
        "ltv": 252,  # 15 * 24 * 0.70 = $252
    },
    "payback_period": {
        "target": 4,  # months
        "calculation": "35 / (15 * 0.70) â‰ˆ 3.3 months",
    },
    "ltv_cac_ratio": {
        "target": 3.0,  # Industry standard for SaaS
        "actual": 7.2,  # 252 / 35 = 7.2 (excellent)
    },
}

# ===== GO-TO-MARKET STRATEGY (90 DAYS) =====
GTM_ROADMAP = {
    "phase_1": {
        "name": "Private Beta & Product-Market Fit",
        "duration": "Days 1-30",
        "goals": [
            "Recruit 100 researchers for private beta",
            "Achieve 40% Day-7 activation",
            "Validate core value proposition",
            "Refine UX based on feedback",
        ],
        "tactics": [
            "Recruit via Academic Twitter, Reddit (r/PhD, r/GradSchool)",
            "Partner with 3 university research labs",
            "Daily user interviews (5 per week)",
            "Ship 2 feature updates per week based on feedback",
        ],
        "metrics": {
            "signups": 100,
            "activation_rate": 0.40,
            "avg_knowledge_graph_size": 50,  # nodes
            "nps": 40,
        },
        "budget": 5000,  # USD
    },
    "phase_2": {
        "name": "Public Launch & Awareness",
        "duration": "Days 31-60",
        "goals": [
            "Product Hunt #1 Product of the Day",
            "1,000 sign-ups in first week",
            "Establish SEO foundation",
            "Build early case studies",
        ],
        "tactics": [
            "Product Hunt launch (Tuesday, optimized)",
            'Launch blog: "How PhD students finish lit reviews 60% faster"',
            'SEO content: 10 articles targeting "AI research tools"',
            "Partnerships: ResearchGate, Academia.edu newsletters",
            "Reddit AMAs on r/PhD, r/AskAcademia",
        ],
        "metrics": {
            "signups": 1000,
            "product_hunt_ranking": 1,
            "free_to_paid": 0.08,  # 8% (lower than target, early days)
            "cac_blended": 45,  # Slightly above target
        },
        "budget": 15000,
    },
    "phase_3": {
        "name": "Paid Acquisition & Scaling",
        "duration": "Days 61-90",
        "goals": [
            "5,000 total users",
            "10% free-to-paid conversion",
            "CAC payback < 4 months",
            "Prepare for Series A fundraising",
        ],
        "tactics": [
            'Google Ads: High-intent keywords ("AI literature review tool")',
            "Referral program: 1 month free for 3 successful referrals",
            "Influencer partnerships: Academic YouTubers",
            "Conference presence: ACM, IEEE researcher events",
            "PR push: TechCrunch, The Verge coverage",
        ],
        "metrics": {
            "signups_total": 5000,
            "paying_customers": 500,  # 10% conversion
            "mrr": 7500,  # $15 * 500 = $7,500 MRR
            "cac_optimized": 35,
            "payback_months": 3.3,
        },
        "budget": 30000,
    },
}

# ===== SUCCESS METRICS =====
SUCCESS_METRICS = {
    "north_star": {
        "metric": "Knowledge Graph Nodes per User",
        "rationale": "Measures depth of engagement and switching costs",
        "target": 200,  # nodes in first 3 months
        "current": 0,
    },
    "acquisition": {
        "total_signups": {"target": 5000, "q1": 1250},
        "organic_percentage": {"target": 0.60, "q1": 0.40},
        "cac": {"target": 35, "q1": 45},
    },
    "activation": {
        "signup_to_first_synthesis": {"target": 0.40, "q1": 0.30},
        "day_7_retention": {"target": 0.35, "q1": 0.25},
        "time_to_first_value": {"target": 300, "q1": 600},  # seconds
    },
    "monetization": {
        "free_to_paid": {"target": 0.10, "q1": 0.08},
        "arpu": {"target": 15, "q1": 15},
        "churn_monthly": {"target": 0.05, "q1": 0.08},
    },
    "retention": {
        "day_30": {"target": 0.25, "q1": 0.18},
        "day_90": {"target": 0.15, "q1": 0.10},
    },
    "engagement": {
        "dau_mau_ratio": {"target": 0.30, "q1": 0.20},
        "avg_sessions_per_week": {"target": 4, "q1": 3},
        "knowledge_graph_growth": {"target": 20, "q1": 10},  # nodes per month
    },
}

# ===== FINANCIAL PROJECTIONS (12 MONTHS) =====
FINANCIAL_PROJECTIONS = {
    "month_1": {"users": 100, "paying": 5, "mrr": 75, "costs": 8000},
    "month_2": {"users": 1100, "paying": 80, "mrr": 1200, "costs": 22000},
    "month_3": {"users": 5000, "paying": 500, "mrr": 7500, "costs": 38000},
    "month_6": {"users": 15000, "paying": 1800, "mrr": 27000, "costs": 55000},
    "month_12": {"users": 50000, "paying": 6000, "mrr": 90000, "costs": 80000},
}

# ===== SWOT ANALYSIS (Our Product) =====
OUR_SWOT = {
    "strengths": [
        "Vertical focus on research synthesis (unique positioning)",
        "Deep academic database integration",
        "Knowledge graph compounds switching costs",
        "Premium pricing justified by specialist value",
        "Founder has PhD background (domain expertise)",
    ],
    "weaknesses": [
        "New entrant (no brand recognition)",
        "Smaller team vs Notion (30 vs 200+)",
        "Limited funding compared to competitors",
        "No existing user base to cross-sell",
        "Research workflow requires education (long sales cycle)",
    ],
    "opportunities": [
        "AI productivity market growing 150% YoY",
        "Academic researchers underserved (no specialist tool)",
        "API costs declining (improving margins)",
        "Remote work increasing research collaboration needs",
        "Expand to consultants/journalists after PMF",
    ],
    "threats": [
        "Notion AI could add research features (large distribution)",
        "ChatGPT $20/month bundles many use cases",
        "University budget cuts reduce tool spending",
        "Privacy concerns (researchers need data security)",
        "Switching costs work both ways (hard to migrate users from competitors)",
    ],
}

# ===== VISUALIZATION SETTINGS =====
COLOR_SCHEME = {
    "primary": "#6366f1",  # Indigo (tech/AI feel)
    "secondary": "#8b5cf6",  # Purple
    "accent": "#ec4899",  # Pink
    "info": "#3b82f6",  # Blue
    "success": "#10b981",  # Green
    "warning": "#f59e0b",  # Amber
    "danger": "#ef4444",  # Red
    "background": "#f9fafb",  # Light gray
    "text": "#111827",  # Dark gray
}

CHART_STYLE = {
    "font_family": 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
    "title_size": 16,
    "label_size": 12,
    "dpi": 300,
}

print("✅ Configuration loaded successfully")
print(f"📁 Project Root: {PROJECT_ROOT}")
print(f"🎯 Product: {PRODUCT_NAME}")
print(f"📊 Target Market: {TARGET_MARKET['primary']['size']:,} users")
print(
    f"💰 Revenue Potential: ${MARKET_SIZE['som']['size'] * 15 * 0.10 / 1_000_000:.0f}M ARR at 10% conversion"
)
