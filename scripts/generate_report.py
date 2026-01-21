"""
Report Generation Script
Generates all strategy reports without running full analysis
"""

import sys
from pathlib import Path
import pandas as pd

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from competitive_analyzer import CompetitiveAnalyzer
from market_sizer import MarketSizer
from pricing_strategy import PricingStrategy
from gtm_planner import GTMPlanner
from financial_model import FinancialModel
from config import *


def main():
    print("=" * 80)
    print(" REPORT GENERATION SCRIPT")
    print("=" * 80)
    print()

    # Check if data exists
    required_files = [
        PROCESSED_DATA_DIR / "competitive_overview.csv",
        PROCESSED_DATA_DIR / "feature_matrix.csv",
        PROCESSED_DATA_DIR / "positioning_data.csv",
        PROCESSED_DATA_DIR / "financial_projections_24m.csv",
    ]

    missing_files = [f for f in required_files if not f.exists()]

    if missing_files:
        print("❌ Missing required data files:")
        for f in missing_files:
            print(f"   - {f.name}")
        print()
        print("Please run data collection first:")
        print("  python scripts/run_full_analysis.py")
        print()
        return

    print("✅ All required data files found")
    print()

    # Load data
    print("Loading data...")
    competitors_df = pd.read_csv(PROCESSED_DATA_DIR / "competitive_overview.csv")
    features_matrix = pd.read_csv(PROCESSED_DATA_DIR / "feature_matrix.csv")
    positioning = pd.read_csv(PROCESSED_DATA_DIR / "positioning_data.csv")
    financial = pd.read_csv(PROCESSED_DATA_DIR / "financial_projections_24m.csv")

    print("✅ Data loaded successfully")
    print()

    # Generate reports
    print("-" * 80)
    print("Generating Reports")
    print("-" * 80)
    print()

    # 1. Competitive Analysis Report
    print("1. Competitive Analysis Summary...")
    analyzer = CompetitiveAnalyzer(competitors_df, features_matrix)
    analyzer.positioning_data = positioning
    summary = analyzer.generate_competitive_summary()

    with open(
        REPORTS_DIR / "competitive_analysis_summary.txt", "w", encoding="utf-8"
    ) as f:
        f.write(summary)
    print("   ✅ Saved: competitive_analysis_summary.txt")

    # 2. Market Sizing Report
    print("\n2. Market Sizing Report...")
    sizer = MarketSizer()
    sizer.calculate_tam()
    sizer.calculate_sam()
    sizer.calculate_som()
    report = sizer.generate_market_sizing_report()

    with open(REPORTS_DIR / "market_sizing_report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    print("   ✅ Saved: market_sizing_report.txt")

    # 3. Pricing Strategy Report
    print("\n3. Pricing Strategy Recommendation...")
    strategy = PricingStrategy()
    strategy.analyze_competitor_pricing(competitors_df)
    strategy.calculate_value_metrics()
    strategy.validate_unit_economics()
    pricing_report = strategy.generate_pricing_recommendation()

    with open(
        REPORTS_DIR / "pricing_strategy_recommendation.txt", "w", encoding="utf-8"
    ) as f:
        f.write(pricing_report)
    print("   ✅ Saved: pricing_strategy_recommendation.txt")

    # 4. GTM Strategy Report
    print("\n4. GTM Strategy Report...")
    planner = GTMPlanner()
    planner.create_weekly_breakdown()
    planner.define_channel_strategy()
    gtm_report = planner.generate_gtm_report()

    with open(REPORTS_DIR / "gtm_strategy_report.txt", "w", encoding="utf-8") as f:
        f.write(gtm_report)
    print("   ✅ Saved: gtm_strategy_report.txt")

    # 5. Financial Model Report
    print("\n5. Financial Projections Report...")
    model = FinancialModel()
    model.monthly_projections = financial
    model.calculate_break_even()
    financial_report = model.generate_financial_report()

    with open(REPORTS_DIR / "financial_model_report.txt", "w", encoding="utf-8") as f:
        f.write(financial_report)
    print("   ✅ Saved: financial_model_report.txt")

    print()
    print("=" * 80)
    print(" REPORT GENERATION COMPLETE")
    print("=" * 80)
    print()
    print(f"📁 All reports saved to: {REPORTS_DIR}")
    print()
    print("Generated reports:")
    print("  1. competitive_analysis_summary.txt")
    print("  2. market_sizing_report.txt")
    print("  3. pricing_strategy_recommendation.txt")
    print("  4. gtm_strategy_report.txt")
    print("  5. financial_model_report.txt")
    print()
    print("Next steps:")
    print("  - Review reports in outputs/reports/")
    print("  - Launch dashboard: streamlit run app/streamlit_app.py")
    print()


if __name__ == "__main__":
    main()
