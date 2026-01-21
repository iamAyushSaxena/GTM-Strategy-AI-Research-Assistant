"""
Pricing Strategy & Unit Economics
Calculate optimal pricing and validate business model
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from config import *


class PricingStrategy:
    """
    Develops pricing strategy and validates unit economics
    """

    def __init__(self):
        self.pricing_tiers = PRICING_TIERS
        self.unit_economics = UNIT_ECONOMICS
        self.competitor_pricing = None
        self.value_metric_analysis = None

    def analyze_competitor_pricing(self, competitors_df: pd.DataFrame) -> pd.DataFrame:
        """
        Analyze competitor pricing strategies
        """
        print("💰 Analyzing competitor pricing...")

        pricing_data = []

        for key, comp in COMPETITORS.items():
            # Extract pricing tiers
            pricing = comp["pricing"]

            for tier_name, price in pricing.items():
                if isinstance(price, (int, float)):
                    pricing_data.append(
                        {
                            "competitor_id": key,
                            "competitor_name": comp["name"],
                            "tier": tier_name,
                            "price_monthly": price,
                            "has_free_tier": pricing.get("free", False),
                            "positioning": comp["positioning"],
                        }
                    )

        self.competitor_pricing = pd.DataFrame(pricing_data)

        # Calculate statistics
        print(f"✅ Analyzed pricing for {len(COMPETITORS)} competitors")
        print(
            f"   Average paid tier: ${self.competitor_pricing[self.competitor_pricing['price_monthly'] > 0]['price_monthly'].mean():.2f}/month"
        )
        print(
            f"   Median paid tier: ${self.competitor_pricing[self.competitor_pricing['price_monthly'] > 0]['price_monthly'].median():.2f}/month"
        )
        print(
            f"   Range: ${self.competitor_pricing[self.competitor_pricing['price_monthly'] > 0]['price_monthly'].min():.0f} - ${self.competitor_pricing[self.competitor_pricing['price_monthly'] > 0]['price_monthly'].max():.0f}"
        )

        return self.competitor_pricing

    def calculate_value_metrics(self) -> Dict:
        """
        Calculate value metrics that justify pricing
        """
        print("📊 Calculating value metrics...")

        # Time savings analysis
        time_savings = {
            "manual_literature_review": {
                "hours_per_paper": 2.0,  # Hours to read and synthesize one paper
                "papers_per_review": 50,  # Average papers in a literature review
                "total_hours": 100,
                "hourly_value": 50,  # PhD student/researcher hourly rate
                "total_value": 5000,
            },
            "with_our_tool": {
                "hours_per_paper": 0.5,  # AI reads and synthesizes
                "papers_per_review": 50,
                "total_hours": 25,
                "time_saved_hours": 75,
                "value_saved": 3750,
            },
            "monthly_reviews": 0.5,  # Assume 1 review every 2 months
            "monthly_value_saved": 1875,  # $3750 / 2 months
        }

        # Calculate ROI
        our_pricing = {
            "monthly_cost": PRICING_TIERS["pro"]["price_monthly"],
            "annual_cost": PRICING_TIERS["pro"]["price_annual"],
        }

        roi_analysis = {
            "monthly_value_delivered": time_savings["monthly_value_saved"],
            "monthly_cost": our_pricing["monthly_cost"],
            "monthly_roi": (
                time_savings["monthly_value_saved"] - our_pricing["monthly_cost"]
            )
            / our_pricing["monthly_cost"],
            "payback_hours": our_pricing["monthly_cost"]
            / 50,  # Hours of work to pay for tool
            "value_prop": f"Save {time_savings['with_our_tool']['time_saved_hours']} hours per literature review",
        }

        # Willingness to pay analysis
        willingness_to_pay = {
            "reference_points": {
                "netflix": 15.99,
                "spotify": 10.99,
                "chatgpt_plus": 20.00,
                "notion_pro": 10.00,
                "grammarly_premium": 12.00,
            },
            "average_productivity_tool": 12.50,
            "premium_category": 15.00,  # Tools that save professional time
            "our_positioning": PRICING_TIERS["pro"]["price_monthly"],
            "premium_vs_avg": PRICING_TIERS["pro"]["price_monthly"] / 12.50,
        }

        self.value_metric_analysis = {
            "time_savings": time_savings,
            "roi": roi_analysis,
            "willingness_to_pay": willingness_to_pay,
            "justification": f"At ${our_pricing['monthly_cost']}/month, tool delivers ${roi_analysis['monthly_value_delivered']:.0f} in value = {roi_analysis['monthly_roi']*100:.0f}% ROI",
        }

        print(f"✅ Value metrics calculated")
        print(
            f"   Monthly value delivered: ${roi_analysis['monthly_value_delivered']:.0f}"
        )
        print(f"   Monthly cost: ${our_pricing['monthly_cost']}")
        print(f"   ROI: {roi_analysis['monthly_roi']*100:.0f}%")

        return self.value_metric_analysis

    def validate_unit_economics(self, assumptions: Dict = None) -> Dict:
        """
        Validate unit economics and calculate key metrics

        Args:
            assumptions: Override default assumptions
        """
        print("🧮 Validating unit economics...")

        if assumptions is None:
            assumptions = {}

        # Cost structure
        costs = {
            "cogs": {
                "openai_api_per_user": assumptions.get(
                    "api_cost", 3.50
                ),  # $3.50/user/month (GPT-4)
                "infrastructure_per_user": assumptions.get(
                    "infra_cost", 0.50
                ),  # AWS, storage
                "total_per_user": 4.00,
            },
            "gross_margin": 1 - (4.00 / PRICING_TIERS["pro"]["price_monthly"]),
            "operating_costs": {
                "product_development": assumptions.get("dev_cost", 25000),  # Monthly
                "sales_marketing": assumptions.get("marketing_cost", 30000),
                "general_admin": assumptions.get("admin_cost", 15000),
                "total_monthly": 70000,
            },
        }

        # Customer economics
        customer_economics = {
            "arpu": UNIT_ECONOMICS["ltv"]["arpu"],
            "gross_margin_pct": costs["gross_margin"],
            "gross_profit_per_user": UNIT_ECONOMICS["ltv"]["arpu"]
            * costs["gross_margin"],
            "retention_rate_monthly": assumptions.get("retention", 0.95),  # 5% churn
            "avg_lifetime_months": 1 / (1 - 0.95),  # ~20 months
            "ltv": UNIT_ECONOMICS["ltv"]["arpu"]
            * (1 / (1 - 0.95))
            * costs["gross_margin"],
        }

        # CAC analysis
        cac_analysis = {
            "blended_cac": UNIT_ECONOMICS["cac"]["blended"],
            "ltv": customer_economics["ltv"],
            "ltv_cac_ratio": customer_economics["ltv"]
            / UNIT_ECONOMICS["cac"]["blended"],
            "payback_period_months": UNIT_ECONOMICS["cac"]["blended"]
            / customer_economics["gross_profit_per_user"],
            "magic_number": customer_economics["gross_profit_per_user"]
            * 12
            / UNIT_ECONOMICS["cac"]["blended"],
        }

        # Break-even analysis
        breakeven = {
            "monthly_fixed_costs": costs["operating_costs"]["total_monthly"],
            "gross_profit_per_user": customer_economics["gross_profit_per_user"],
            "users_needed_for_breakeven": int(
                costs["operating_costs"]["total_monthly"]
                / customer_economics["gross_profit_per_user"]
            ),
            "mrr_needed": costs["operating_costs"]["total_monthly"]
            / costs["gross_margin"],
        }

        validation = {
            "costs": costs,
            "customer_economics": customer_economics,
            "cac_analysis": cac_analysis,
            "breakeven": breakeven,
            "health_check": {
                "ltv_cac_ratio": {
                    "value": cac_analysis["ltv_cac_ratio"],
                    "target": 3.0,
                    "status": (
                        "Excellent"
                        if cac_analysis["ltv_cac_ratio"] > 3
                        else "Needs Improvement"
                    ),
                },
                "payback_period": {
                    "value": cac_analysis["payback_period_months"],
                    "target": 12,  # < 12 months
                    "status": (
                        "Excellent"
                        if cac_analysis["payback_period_months"] < 12
                        else "Needs Improvement"
                    ),
                },
                "gross_margin": {
                    "value": costs["gross_margin"],
                    "target": 0.70,  # >70%
                    "status": (
                        "Excellent"
                        if costs["gross_margin"] > 0.70
                        else "Good" if costs["gross_margin"] > 0.60 else "Poor"
                    ),
                },
            },
        }

        print(f"✅ Unit economics validated")
        print(
            f"   LTV/CAC Ratio: {cac_analysis['ltv_cac_ratio']:.1f}x ({validation['health_check']['ltv_cac_ratio']['status']})"
        )
        print(
            f"   Payback Period: {cac_analysis['payback_period_months']:.1f} months ({validation['health_check']['payback_period']['status']})"
        )
        print(
            f"   Gross Margin: {costs['gross_margin']*100:.1f}% ({validation['health_check']['gross_margin']['status']})"
        )
        print(
            f"   Break-even: {breakeven['users_needed_for_breakeven']:,} paying users"
        )

        return validation

    def generate_pricing_recommendation(self) -> str:
        """
        Generate pricing strategy recommendation
        """
        if self.competitor_pricing is None:
            # Create dummy data for standalone execution
            self.competitor_pricing = pd.DataFrame(
                [
                    {"competitor_name": "Notion AI", "price_monthly": 10},
                    {"competitor_name": "Mem.ai", "price_monthly": 8},
                    {"competitor_name": "Reflect", "price_monthly": 10},
                ]
            )

        if self.value_metric_analysis is None:
            self.calculate_value_metrics()

        unit_econ = self.validate_unit_economics()

        report = "=" * 80 + "\n"
        report += "PRICING STRATEGY RECOMMENDATION\n"
        report += "=" * 80 + "\n\n"

        report += "💰 PROPOSED PRICING TIERS\n"
        report += "-" * 80 + "\n"
        for tier_name, tier_data in PRICING_TIERS.items():
            report += f"\n{tier_data['name'].upper()} TIER\n"
            if tier_data.get("price_monthly", 0) == 0:
                report += f"   Price: FREE\n"
            else:
                report += f"   Price: ${tier_data['price_monthly']}/month (${tier_data.get('price_annual', tier_data['price_monthly']*12)}/year)\n"
            report += f"   Features:\n"
            for feature in tier_data["features"]:
                report += f"      • {feature}\n"
            if "target_segment" in tier_data:
                report += f"   Target: {tier_data['target_segment']}\n"
            if "value_prop" in tier_data:
                report += f"   Value Prop: {tier_data['value_prop']}\n"

        report += "\n\n"
        report += "📊 COMPETITIVE POSITIONING\n"
        report += "-" * 80 + "\n"
        avg_competitor = self.competitor_pricing[
            self.competitor_pricing["price_monthly"] > 0
        ]["price_monthly"].mean()
        our_price = PRICING_TIERS["pro"]["price_monthly"]
        premium = (our_price - avg_competitor) / avg_competitor

        report += f"Average Competitor Price: ${avg_competitor:.2f}/month\n"
        report += f"Our Price (Pro Tier): ${our_price:.2f}/month\n"
        report += f"Premium vs Average: {premium*100:+.1f}%\n"
        report += f"\nRationale for Premium:\n"
        report += (
            f"   • Vertical specialization (research synthesis) vs horizontal tools\n"
        )
        report += f"   • Deep academic database integration (unique value)\n"
        report += f"   • Delivers ${self.value_metric_analysis['roi']['monthly_value_delivered']:.0f}/month in value\n"
        report += f"   • ROI: {self.value_metric_analysis['roi']['monthly_roi']*100:.0f}% monthly\n"

        report += "\n\n"
        report += "🧮 UNIT ECONOMICS VALIDATION\n"
        report += "-" * 80 + "\n"
        report += f"Customer Lifetime Value (LTV): ${unit_econ['customer_economics']['ltv']:.2f}\n"
        report += f"Customer Acquisition Cost (CAC): ${unit_econ['cac_analysis']['blended_cac']:.2f}\n"
        report += f"LTV/CAC Ratio: {unit_econ['cac_analysis']['ltv_cac_ratio']:.1f}x ({unit_econ['health_check']['ltv_cac_ratio']['status']})\n"
        report += f"Payback Period: {unit_econ['cac_analysis']['payback_period_months']:.1f} months ({unit_econ['health_check']['payback_period']['status']})\n"
        report += f"Gross Margin: {unit_econ['costs']['gross_margin']*100:.1f}% ({unit_econ['health_check']['gross_margin']['status']})\n"
        report += f"\n"
        report += f"Break-even Analysis:\n"
        report += f"   Monthly Fixed Costs: ${unit_econ['breakeven']['monthly_fixed_costs']:,}\n"
        report += f"   Paying Users Needed: {unit_econ['breakeven']['users_needed_for_breakeven']:,}\n"
        report += f"   MRR Required: ${unit_econ['breakeven']['mrr_needed']:,.0f}\n"

        report += "\n\n"
        report += "✅ STRATEGIC RECOMMENDATIONS\n"
        report += "-" * 80 + "\n"
        report += "1. PRICING TIER STRATEGY\n"
        report += "   • Launch with 3 tiers: Free, Pro ($15), Team ($30)\n"
        report += "   • Free tier is generous (50 documents) to drive virality\n"
        report += "   • Pro tier targets individual researchers (80% of market)\n"
        report += "   • Team tier for research labs (20% of market, 2x ARPU)\n"
        report += "\n"
        report += "2. FREE-TO-PAID CONVERSION\n"
        report += "   • Target: 10% conversion rate in first 6 months\n"
        report += "   • Tactics: Email nurture, usage-based upgrades, social proof\n"
        report += (
            "   • Trigger: When user hits 50 document limit or needs citation export\n"
        )
        report += "\n"
        report += "3. PRICING TESTS TO RUN\n"
        report += "   • Test $12 vs $15 vs $18 for Pro tier\n"
        report += "   • Test annual discount (20% vs 25% vs 30%)\n"
        report += "   • Test freemium limit (25 vs 50 vs 100 documents)\n"
        report += "\n"
        report += "4. ANNUAL PREPAY INCENTIVE\n"
        report += "   • Offer 20% discount for annual prepay ($144 vs $180)\n"
        report += "   • Improves cash flow and reduces churn\n"
        report += "   • Target 40% of paid users on annual plans\n"
        report += "\n"
        report += "5. REGIONAL PRICING STRATEGY (INDIA FOCUS)\n"
        report += "   • Problem: Standard $15/mo is high friction for Indian market (~₹1,250)\n"
        report += "   • Strategy: Implement Purchasing Power Parity (PPP) pricing\n"
        report += "   • Offer: Pro Plan at ₹499/month (approx $6) for users in India\n"
        report += "   • Rationale: Lower barrier to entry for large volume of Indian PhD scholars\n"
        report += "   • Impact: Increases adoption in the beachhead market while maintaining global ARPU\n"

        return report


if __name__ == "__main__":
    print("=" * 80)
    print(" PRICING STRATEGY ANALYZER")
    print("=" * 80)
    print()

    strategy = PricingStrategy()

    # Load competitor data
    try:
        competitors_df = pd.read_csv(PROCESSED_DATA_DIR / "competitive_overview.csv")
        strategy.analyze_competitor_pricing(competitors_df)
    except FileNotFoundError:
        print("⚠️  Competitor data not found, using defaults")

    # Calculate value metrics
    strategy.calculate_value_metrics()

    # Validate unit economics
    strategy.validate_unit_economics()

    # Generate recommendation
    recommendation = strategy.generate_pricing_recommendation()
    print("\n" + recommendation)

    # Save report
    with open(REPORTS_DIR / "pricing_strategy_recommendation.txt", "w") as f:
        f.write(recommendation)

    print("\n💾 Report saved to:", REPORTS_DIR / "pricing_strategy_recommendation.txt")
    print("✅ Pricing strategy analysis complete!")
