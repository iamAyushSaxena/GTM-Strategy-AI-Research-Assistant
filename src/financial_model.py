"""
Financial Model & Projections
Revenue forecasting and path to profitability
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
from config import *


class FinancialModel:
    """
    Creates financial projections and validates business model
    """
    
    def __init__(self):
        self.monthly_projections = None
        self.revenue_model = None
        self.profitability_analysis = None
        
    def project_user_growth(self, months: int = 24) -> pd.DataFrame:
        """
        Project user growth over time
        
        Args:
            months: Number of months to project
        """
        print(f"📈 Projecting user growth for {months} months...")
        
        projections = []
        
        # Starting conditions
        current_users = 0
        current_paying = 0
        
        for month in range(1, months + 1):
            # Month-specific growth assumptions
            if month <= 3:
                # Phase 1-2: GTM launch period (high growth)
                monthly_signups = FINANCIAL_PROJECTIONS[f'month_{month}']['users']
                viral_coefficient = 0.15  # Low initially
                churn_rate = 0.08  # Higher in early days
            elif month <= 6:
                # Phase 3: Scaling period
                monthly_signups = 3000 * (1.20 ** (month - 3))  # 20% monthly growth
                viral_coefficient = 0.25  # Improving virality
                churn_rate = 0.06
            elif month <= 12:
                # Growth phase
                monthly_signups = 5000 * (1.15 ** (month - 6))  # 15% monthly growth
                viral_coefficient = 0.30
                churn_rate = 0.05
            else:
                # Mature phase
                monthly_signups = 8000 * (1.10 ** (month - 12))  # 10% monthly growth
                viral_coefficient = 0.35
                churn_rate = 0.04
            
            # Add viral signups
            viral_signups = int(current_users * viral_coefficient)
            total_new_users = int(monthly_signups + viral_signups)
            
            # Calculate cumulative users (accounting for churn)
            churned_users = int(current_users * churn_rate)
            current_users = current_users + total_new_users - churned_users
            
            # Calculate paying users
            if month <= 3:
                free_to_paid_rate = 0.05 + (month * 0.015)  # Ramping up: 5% -> 8%
            else:
                free_to_paid_rate = min(0.10, 0.08 + ((month - 3) * 0.003))  # Approaching 10%
            
            new_paying = int(total_new_users * free_to_paid_rate)
            churned_paying = int(current_paying * churn_rate * 0.5)  # Paying users churn less
            current_paying = current_paying + new_paying - churned_paying
            
            # Calculate revenue
            arpu = PRICING_TIERS['pro']['price_monthly']
            mrr = current_paying * arpu
            arr = mrr * 12
            
            # Calculate costs
            # COGS scales with users
            api_costs = current_users * 3.50  # $3.50/user/month for AI API
            infra_costs = current_users * 0.50  # $0.50/user/month for infrastructure
            total_cogs = api_costs + infra_costs
            
            # Operating costs (mostly fixed, some scaling)
            if month <= 6:
                product_dev = 25000
                sales_marketing = 20000 + (month * 3000)  # Scaling marketing
                general_admin = 15000
            else:
                product_dev = 30000 + ((month - 6) * 2000)  # Hiring more engineers
                sales_marketing = 40000 + ((month - 6) * 5000)
                general_admin = 20000 + ((month - 6) * 1000)
            
            total_opex = product_dev + sales_marketing + general_admin
            total_costs = total_cogs + total_opex
            
            # Profitability
            gross_profit = mrr - total_cogs
            net_profit = mrr - total_costs
            gross_margin = gross_profit / mrr if mrr > 0 else 0
            
            # CAC calculation (blend of channels)
            cac_by_month = {
                1: 60, 2: 55, 3: 50,  # Optimizing
                6: 40, 12: 35, 18: 32, 24: 30  # Economies of scale
            }
            blended_cac = cac_by_month.get(month, 35)
            
            # LTV calculation
            avg_lifetime_months = 1 / (churn_rate if churn_rate > 0 else 0.05)
            ltv = arpu * avg_lifetime_months * gross_margin
            
            projections.append({
                'month': month,
                'date': (datetime.now() + timedelta(days=30*month)).strftime('%Y-%m'),
                'total_users': current_users,
                'new_users': total_new_users,
                'viral_signups': viral_signups,
                'churned_users': churned_users,
                'paying_users': current_paying,
                'new_paying': new_paying,
                'free_to_paid_rate': free_to_paid_rate,
                'churn_rate': churn_rate,
                'mrr': mrr,
                'arr': arr,
                'arpu': arpu,
                'total_cogs': total_cogs,
                'gross_profit': gross_profit,
                'gross_margin': gross_margin,
                'opex': total_opex,
                'net_profit': net_profit,
                'cac': blended_cac,
                'ltv': ltv,
                'ltv_cac_ratio': ltv / blended_cac if blended_cac > 0 else 0
            })
        
        self.monthly_projections = pd.DataFrame(projections)
        
        print(f"✅ Projected growth for {months} months")
        print(f"   Month 12: {self.monthly_projections.iloc[11]['total_users']:,.0f} users, ${self.monthly_projections.iloc[11]['mrr']:,.0f} MRR")
        print(f"   Month 24: {self.monthly_projections.iloc[23]['total_users']:,.0f} users, ${self.monthly_projections.iloc[23]['mrr']:,.0f} MRR")
        
        return self.monthly_projections
    
    def calculate_break_even(self) -> Dict:
        """
        Calculate when company reaches break-even
        """
        print("💰 Calculating break-even point...")
        
        if self.monthly_projections is None:
            self.project_user_growth()
        
        # Find first month with positive net profit
        profitable_months = self.monthly_projections[
            self.monthly_projections['net_profit'] > 0
        ]
        
        if len(profitable_months) > 0:
            breakeven_month = profitable_months.iloc[0]['month']
            breakeven_data = profitable_months.iloc[0]
            
            breakeven_analysis = {
                'month': int(breakeven_month),
                'date': breakeven_data['date'],
                'users_at_breakeven': int(breakeven_data['total_users']),
                'paying_users_at_breakeven': int(breakeven_data['paying_users']),
                'mrr_at_breakeven': float(breakeven_data['mrr']),
                'reached': True
            }
        else:
            breakeven_analysis = {
                'month': None,
                'date': None,
                'users_at_breakeven': None,
                'paying_users_at_breakeven': None,
                'mrr_at_breakeven': None,
                'reached': False,
                'note': 'Break-even not reached within projection period'
            }
        
        self.profitability_analysis = breakeven_analysis
        
        if breakeven_analysis['reached']:
            print(f"✅ Break-even reached at Month {breakeven_analysis['month']}")
            print(f"   Users: {breakeven_analysis['users_at_breakeven']:,}")
            print(f"   MRR: ${breakeven_analysis['mrr_at_breakeven']:,.0f}")
        else:
            print(f"⚠️  Break-even not reached within 24 months")
        
        return breakeven_analysis
    
    def generate_financial_report(self) -> str:
        """
        Generate comprehensive financial report
        """
        if self.monthly_projections is None:
            self.project_user_growth(24)
        
        if self.profitability_analysis is None:
            self.calculate_break_even()
        
        report = "=" * 80 + "\n"
        report += "FINANCIAL MODEL & PROJECTIONS (24 MONTHS)\n"
        report += "=" * 80 + "\n\n"
        
        report += "📊 KEY MILESTONES\n"
        report += "-" * 80 + "\n"
        
        # Month 3 (End of GTM)
        m3 = self.monthly_projections.iloc[2]
        report += f"MONTH 3 (End of 90-Day GTM):\n"
        report += f"   Total Users: {m3['total_users']:,.0f}\n"
        report += f"   Paying Users: {m3['paying_users']:,.0f}\n"
        report += f"   MRR: ${m3['mrr']:,.0f}\n"
        report += f"   ARR: ${m3['arr']:,.0f}\n"
        report += f"   Free-to-Paid: {m3['free_to_paid_rate']*100:.1f}%\n"
        report += f"   Gross Margin: {m3['gross_margin']*100:.1f}%\n"
        report += f"   Net Profit: ${m3['net_profit']:,.0f}\n\n"
        
        # Month 6
        m6 = self.monthly_projections.iloc[5]
        report += f"MONTH 6 (Scaling Phase):\n"
        report += f"   Total Users: {m6['total_users']:,.0f}\n"
        report += f"   Paying Users: {m6['paying_users']:,.0f}\n"
        report += f"   MRR: ${m6['mrr']:,.0f}\n"
        report += f"   ARR: ${m6['arr']:,.0f}\n"
        report += f"   Churn Rate: {m6['churn_rate']*100:.1f}%\n"
        report += f"   LTV/CAC: {m6['ltv_cac_ratio']:.1f}x\n"
        report += f"   Net Profit: ${m6['net_profit']:,.0f}\n\n"
        
        # Month 12 (End of Year 1)
        m12 = self.monthly_projections.iloc[11]
        report += f"MONTH 12 (End of Year 1):\n"
        report += f"   Total Users: {m12['total_users']:,.0f}\n"
        report += f"   Paying Users: {m12['paying_users']:,.0f}\n"
        report += f"   MRR: ${m12['mrr']:,.0f}\n"
        report += f"   ARR: ${m12['arr']:,.0f}\n"
        report += f"   Gross Profit: ${m12['gross_profit']:,.0f}\n"
        report += f"   Net Profit: ${m12['net_profit']:,.0f}\n\n"
        
        # Month 24 (End of Year 2)
        m24 = self.monthly_projections.iloc[23]
        report += f"MONTH 24 (End of Year 2):\n"
        report += f"   Total Users: {m24['total_users']:,.0f}\n"
        report += f"   Paying Users: {m24['paying_users']:,.0f}\n"
        report += f"   MRR: ${m24['mrr']:,.0f}\n"
        report += f"   ARR: ${m24['arr']:,.0f}\n"
        report += f"   Gross Margin: {m24['gross_margin']*100:.1f}%\n"
        report += f"   Net Profit: ${m24['net_profit']:,.0f}\n\n"
        
        report += "💰 BREAK-EVEN ANALYSIS\n"
        report += "-" * 80 + "\n"
        if self.profitability_analysis['reached']:
            report += f"Break-even Month: {self.profitability_analysis['month']}\n"
            report += f"Date: {self.profitability_analysis['date']}\n"
            report += f"Users Required: {self.profitability_analysis['users_at_breakeven']:,}\n"
            report += f"Paying Users: {self.profitability_analysis['paying_users_at_breakeven']:,}\n"
            report += f"MRR at Break-even: ${self.profitability_analysis['mrr_at_breakeven']:,.0f}\n"
        else:
            report += f"Status: {self.profitability_analysis['note']}\n"
            report += f"Note: May need to adjust operating costs or improve unit economics\n"
        
        report += "\n\n"
        report += "📈 GROWTH METRICS SUMMARY\n"
        report += "-" * 80 + "\n"
        
        # Calculate cumulative metrics
        total_revenue_24m = self.monthly_projections['mrr'].sum()
        total_costs_24m = (self.monthly_projections['total_cogs'] + self.monthly_projections['opex']).sum()
        net_income_24m = total_revenue_24m - total_costs_24m
        
        report += f"24-Month Cumulative:\n"
        report += f"   Total Revenue: ${total_revenue_24m:,.0f}\n"
        report += f"   Total Costs: ${total_costs_24m:,.0f}\n"
        report += f"   Net Income: ${net_income_24m:,.0f}\n"
        report += f"\n"
        
        # Growth rates
        m1_users = self.monthly_projections.iloc[0]['total_users']
        m24_users = self.monthly_projections.iloc[23]['total_users']
        user_growth_rate = ((m24_users / m1_users) ** (1/23) - 1) if m1_users > 0 else 0
        
        m1_mrr = self.monthly_projections.iloc[0]['mrr']
        m24_mrr = self.monthly_projections.iloc[23]['mrr']
        revenue_growth_rate = ((m24_mrr / m1_mrr) ** (1/23) - 1) if m1_mrr > 0 else 0
        
        report += f"Average Monthly Growth Rates:\n"
        report += f"   Users: {user_growth_rate*100:.1f}%\n"
        report += f"   Revenue: {revenue_growth_rate*100:.1f}%\n"
        
        report += "\n\n"
        report += "🎯 FUNDRAISING READINESS (Month 12)\n"
        report += "-" * 80 + "\n"
        report += f"ARR: ${m12['arr']:,.0f}\n"
        report += f"Monthly Growth Rate: {(m12['new_users'] / (m12['total_users'] - m12['new_users']))*100:.1f}%\n"
        report += f"Gross Margin: {m12['gross_margin']*100:.1f}%\n"
        report += f"LTV/CAC: {m12['ltv_cac_ratio']:.1f}x\n"
        report += f"Churn Rate: {m12['churn_rate']*100:.1f}%\n"
        report += f"\n"
        
        # Fundraising readiness assessment
        report += "Series A Readiness:\n"
        criteria_met = 0
        total_criteria = 5
        
        if m12['arr'] >= 1_000_000:
            report += f"   ✅ ARR > $1M\n"
            criteria_met += 1
        else:
            report += f"   ❌ ARR > $1M (current: ${m12['arr']:,.0f})\n"
        
        growth_rate = (m12['new_users'] / (m12['total_users'] - m12['new_users']))
        if growth_rate >= 0.10:
            report += f"   ✅ Monthly growth > 10%\n"
            criteria_met += 1
        else:
            report += f"   ❌ Monthly growth > 10% (current: {growth_rate*100:.1f}%)\n"
        
        if m12['gross_margin'] >= 0.70:
            report += f"   ✅ Gross margin > 70%\n"
            criteria_met += 1
        else:
            report += f"   ❌ Gross margin > 70% (current: {m12['gross_margin']*100:.1f}%)\n"
        
        if m12['ltv_cac_ratio'] >= 3.0:
            report += f"   ✅ LTV/CAC > 3.0x\n"
            criteria_met += 1
        else:
            report += f"   ❌ LTV/CAC > 3.0x (current: {m12['ltv_cac_ratio']:.1f}x)\n"
        
        if m12['churn_rate'] <= 0.05:
            report += f"   ✅ Churn < 5%\n"
            criteria_met += 1
        else:
            report += f"   ❌ Churn < 5% (current: {m12['churn_rate']*100:.1f}%)\n"
        
        report += f"\nReadiness Score: {criteria_met}/{total_criteria} criteria met\n"
        
        if criteria_met >= 4:
            report += "Assessment: READY for Series A fundraising\n"
        elif criteria_met >= 3:
            report += "Assessment: Nearly ready - address remaining gaps\n"
        else:
            report += "Assessment: Focus on improving metrics before fundraising\n"
        
        return report


if __name__ == "__main__":
    print("=" * 80)
    print(" FINANCIAL MODEL & PROJECTIONS")
    print("=" * 80)
    print()
    
    model = FinancialModel()
    
    # Project growth
    projections = model.project_user_growth(months=24)
    
    # Calculate break-even
    breakeven = model.calculate_break_even()
    
    # Generate report
    report = model.generate_financial_report()
    print("\n" + report)
    
    # Save outputs
    projections.to_csv(PROCESSED_DATA_DIR / 'financial_projections_24m.csv', index=False)
    
    with open(REPORTS_DIR / 'financial_model_report.txt', 'w') as f:
        f.write(report)
    
    print("\n💾 Outputs saved")
    print("✅ Financial modeling complete!")