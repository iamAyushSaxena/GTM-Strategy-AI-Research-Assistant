# Key Assumptions Document

All assumptions used in the GTM strategy analysis, with rationale and impact assessment.

---

## 1. Market Sizing Assumptions

### TAM (Total Addressable Market)

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| Global knowledge workers do research synthesis | 25% | Based on job description analysis and work activity surveys | TAM could be 15-35% (±40%) | High |
| Knowledge worker population | 1.2B | McKinsey Global Institute 2024 estimate | Well-documented, low variance (±10%) | Low |
| Research synthesis is distinct need | Yes | Literature reviews, competitive analysis, investigative research are dedicated tasks | If wrong, TAM overstated by 50% | Medium |

**TAM Range:** 150M - 450M users (base case: 300M)

---

### SAM (Serviceable Available Market)

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| English-language tool adoption | 20% | English is lingua franca of research, but not universal | Could be 15-30% based on region | High |
| Digital tool adoption rate | 90% | High in developed markets where we'll launch | Well-supported by SaaS penetration data | Low |
| AI tool willingness | 70% | Gartner 2025 survey: 68% of knowledge workers use AI tools | Growing rapidly, could be 80% by 2027 | Medium |
| Paid tool willingness | 60% | Based on freemium SaaS conversion benchmarks | Could be 50-70% depending on value prop | High |

**SAM Range:** 30M - 75M users (base case: 50M)

---

### SOM (Serviceable Obtainable Market)

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| Beachhead: Academic researchers | 13M global | UNESCO + NSF data on PhD students and researchers | Well-documented | Low |
| English-speaking academics | 30% | US, UK, Australia, Canada, Nordic countries, + English as second language | Could be 25-40% | Medium |
| Actively researching | 80% | Not all academics do literature reviews constantly | Could be 70-90% | Low |
| Can capture 10% market share in 12 months | 10% | Aggressive but achievable with strong positioning | Very sensitive: could be 5-15% | **Very High** |

**SOM Range:** 1M - 3M users (base case: 2M)

---

## 2. Pricing Assumptions

### Value Delivered

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| Literature review time (manual) | 100 hours | Average PhD student spends 2-3 months on lit review | Could be 75-150 hours | Medium |
| Researcher hourly value | $50/hour | Mix of PhD stipends ($25/hr) and professor salaries ($75/hr) | Could be $30-80/hour | Medium |
| Time savings with tool | 60% | Based on beta user interviews and similar tool claims | Could be 40-75% | **Very High** |
| Reviews per researcher per month | 0.5 | Some researchers do 1-2/year, others ongoing | Could be 0.3-1.0 | High |

**Value Delivered Range:** $900 - $3,000/month per user

**Pricing Implication:** Even at lower end ($900), $15/month price is only 1.6% of value delivered

---

### Competitive Pricing

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| Vertical tools can command premium | 25% | Historical SaaS data: vertical = 20-40% premium | Well-supported | Low |
| Horizontal average price | $12/month | Average of Notion AI, Mem.ai, Reflect | Publicly available, accurate | Low |
| Price elasticity is low | -0.5 | Research tools are productivity investments, not luxuries | Could be -0.3 to -0.8 | Medium |
| Annual discount attracts 40% of users | 40% | Standard SaaS benchmark | Could be 30-50% | Low |

**Pricing Range:** $12 - $18/month (base case: $15)

---

## 3. Unit Economics Assumptions

### Customer Acquisition Cost (CAC)

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| Product Hunt CAC | $20/user | Based on similar SaaS launches | Could be $15-30 | Medium |
| SEO/Content CAC | $15/user | Long-term channel, includes content production costs | Could be $10-25 | Medium |
| Google Ads CAC | $50/user | High-intent keywords expensive but convert well | Could be $40-80 | **Very High** |
| Referral CAC | $10/user | Cost of incentive (1 month free) | Could be $5-15 | Low |
| Channel mix stays constant | Yes | Assume 40% PH, 30% SEO, 20% Ads, 10% Referral | Mix will shift over time | High |

**Blended CAC Range:** $25 - $50 (base case: $35)

---

### Lifetime Value (LTV)

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| Average Revenue Per User (ARPU) | $15/month | Weighted average of Free ($0), Pro ($15), Team ($30) | Could be $12-18 with different tier mix | Medium |
| Average customer lifetime | 24 months | Based on SaaS benchmarks for productivity tools | Could be 18-36 months | **Very High** |
| Monthly churn rate | 5% | Industry average for SMB SaaS | Could be 3-7% | **Very High** |
| Gross margin | 70% | After API costs ($3.50) and infrastructure ($0.50) | Could be 60-75% as API costs decline | Medium |

**LTV Range:** $180 - $400 (base case: $252)

**LTV/CAC Range:** 3.6x - 16x (base case: 7.2x)

---

### API Costs

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| OpenAI API cost per user | $3.50/month | Based on GPT-4 API pricing and usage estimates | Declining over time (GPT-4 Turbo, future models) | High |
| Average API calls per user | 500/month | Assumes 20 synthesis requests × 25 API calls each | Power users could be 2-3x this | High |
| API costs decline 20%/year | Yes | Historical trend in AI model pricing | Could decline faster with competition | Medium |

**Gross Margin Impact:** Each $1 reduction in API cost = +6.7% gross margin

---

## 4. GTM Strategy Assumptions

### Conversion Funnel

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| Awareness → Sign-up | 20% | Industry benchmark for freemium SaaS | Could be 15-30% based on messaging quality | High |
| Sign-up → Activation | 40% | Activation = create first knowledge graph | Could be 30-50% based on onboarding UX | **Very High** |
| Free → Paid conversion | 10% | Target by month 6; starts at 5% | Could be 5-15%; highly dependent on product value | **Very High** |
| Day 7 retention | 35% | Critical metric for product stickiness | Could be 25-45% | **Very High** |

**User Funnel Example (1,000 aware):**
- Sign-ups: 200 (20%)
- Activated: 80 (40% of sign-ups)
- Paying: 8 (10% of activated)

**Sensitivity:** A 5% improvement in each stage = 2.4x more paying customers

---

### Channel Performance

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| Product Hunt drives 800 users | 800 | Based on similar launches (#1 Product of Day) | Could be 500-1,200 | Medium |
| SEO takes 3 months to ramp | 3 months | Time to rank for competitive keywords | Could be 2-6 months | Low |
| Referral viral coefficient | 0.3 | Each user refers 0.3 new users on average | Could be 0.2-0.5 | High |
| Academic partnerships take 6 weeks | 6 weeks | Time to negotiate and launch | Could be 4-12 weeks | Low |

---

### Timing Assumptions

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| Product ready for beta | Day 1 | Assumes MVP is built | Critical path dependency | **Very High** |
| Can recruit 100 beta users in 4 weeks | Yes | Based on network size and community engagement | Could take 6-8 weeks | Medium |
| Product Hunt launch optimal in Week 6 | Week 6 | After refining product with beta feedback | Could launch Week 4-8 | Low |
| Paid ads effective immediately | Yes | Assumes landing pages and creative are ready | May need 2-4 weeks optimization | Medium |

---

## 5. Financial Projections Assumptions

### Growth Rates

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| Monthly growth rate (M1-3) | 50%+ | Launch period with GTM push | Could be 30-100% | High |
| Monthly growth rate (M4-12) | 15% | Sustained growth phase | Could be 10-25% | High |
| Monthly growth rate (M13-24) | 10% | Mature growth | Could be 5-15% | Medium |
| Growth eventually slows to 5% | Yes | Market saturation and competition | Could maintain 10% longer | Low |

---

### Operating Costs

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| Engineering team size (M1-6) | 3 FTEs | Includes founder + 2 engineers | Could be 2-4 | Medium |
| Engineering team size (M7-12) | 5 FTEs | Scaling team | Could be 4-6 | Medium |
| Marketing spend scales with revenue | 30% of MRR | Reinvesting in growth | Could be 20-40% | High |
| Burn rate without revenue | $60K/month | Covers team + infrastructure | Could be $45-80K | Medium |

**Break-even Sensitivity:**
- If burn is $45K: Break-even at Month 7
- If burn is $80K: Break-even at Month 11
- Base case ($60K): Break-even at Month 9

---

### Churn Assumptions

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| Monthly churn rate (early) | 8% | Higher churn during product iteration | Could be 6-12% | High |
| Monthly churn rate (mature) | 4% | After product-market fit | Could be 3-6% | **Very High** |
| Paying user churn is 50% of free | Yes | Paying users are more committed | Could be 40-70% | Medium |
| Knowledge graph increases retention | +20% | Switching costs compound over time | Core hypothesis; could be +10-30% | **Very High** |

**Impact on LTV:**
- 3% churn → LTV = $350 (+39%)
- 5% churn → LTV = $252 (base case)
- 7% churn → LTV = $193 (-23%)

---

## 6. Product Assumptions

### Feature Development

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| MVP has core features at launch | Yes | Cross-source synthesis, knowledge graph, basic AI | If missing, delays entire GTM | **Critical** |
| Can ship 2 updates/week in beta | Yes | Agile development with small team | Determines feedback velocity | High |
| Academic database integration in V1 | Yes | Key differentiator vs competitors | If delayed, weakens positioning | **Very High** |
| Mobile app not needed for V1 | Correct | Researchers work on desktop/laptop | Could lose mobile-first users | Low |

---

### Technical Assumptions

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| OpenAI API stability | 99%+ uptime | Based on current OpenAI SLA | Downtime would impact UX | Medium |
| Can handle 100K users on current infrastructure | Yes | Cloud-based, scalable architecture | Could need re-architecture | Medium |
| Data privacy complies with GDPR/CCPA | Yes | Legal review completed | Non-compliance is existential risk | **Critical** |

---

## 7. Market Assumptions

### Competitive Landscape

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| No major competitor launches in 12 months | Low probability | Notion, Microsoft could add features | Would compress our window | High |
| Our positioning is defensible | Yes | Vertical focus + knowledge graph moat | If wrong, becomes feature parity race | **Very High** |
| Competitors won't drastically lower prices | Likely | Current pricing is sustainable for them | Price war would hurt margins | Medium |

---

### Academic Market

| Assumption | Value | Rationale | Impact if Wrong | Sensitivity |
|------------|-------|-----------|-----------------|-------------|
| Academics have budget for $15/month tool | Yes | Research grants, university subscriptions | Budget cuts could reduce willingness to pay | Medium |
| Literature reviews remain manual | Yes | No AI has solved this well yet | If someone solves it first, market shrinks | High |
| Researchers want to keep data in cloud | 70% | 30% prefer local-first (Obsidian users) | Affects our addressable market | Medium |

---

## 8. Risk Assessment

### High-Risk Assumptions
**These assumptions have highest impact if wrong:**

1. **10% free-to-paid conversion** (Sensitivity: Very High)
   - Base case: 10%
   - Pessimistic: 5% → Halves revenue
   - Optimistic: 15% → 1.5x revenue

2. **24-month average customer lifetime** (Sensitivity: Very High)
   - Base case: 24 months
   - Pessimistic: 18 months → LTV drops 25%
   - Optimistic: 36 months → LTV increases 50%

3. **Can capture 10% market share in 12 months** (Sensitivity: Very High)
   - Base case: 10%
   - Pessimistic: 5% → Half our user target
   - Optimistic: 15% → 1.5x user target

4. **40% activation rate** (Sensitivity: Very High)
   - Base case: 40%
   - Pessimistic: 25% → Product-market fit issues
   - Optimistic: 55% → Strong PMF signal

5. **Knowledge graph creates switching costs** (Sensitivity: Very High)
   - This is our core moat hypothesis
   - If wrong, we're just another AI note-taking tool

---

## 9. Validation Plan

### How We'll Test Assumptions (First 90 Days)

| Assumption | Validation Method | Timeline | Success Criteria |
|------------|------------------|----------|------------------|
| Researchers value cross-source synthesis | Beta user interviews | Week 1-4 | 70%+ say it's "must have" |
| 40% activation rate achievable | Beta cohort tracking | Week 2-8 | 35%+ activate (ramp to 40%) |
| $15 price point acceptable | Pricing survey + conversion data | Week 6-12 | 8%+ free-to-paid by Week 12 |
| Product Hunt drives 800 users | Launch metrics | Week 6 | 600-1,000 sign-ups in Week 6 |
| Knowledge graph increases retention | Cohort analysis | Week 8-12 | Users with >50 nodes have 50% lower churn |

---

## 10. Assumption Review Schedule

**Monthly Review:**
- Update CAC by channel based on actual data
- Recalculate LTV based on cohort retention
- Adjust growth projections based on trends

**Quarterly Review:**
- Re-assess market size based on new research
- Update competitive landscape
- Revise financial projections

**Triggers for Immediate Review:**
- Major competitor launches similar product
- Conversion rate drops below 5%
- CAC exceeds $50
- Churn exceeds 7%

---

## Summary

**Most Critical Assumptions (Must Validate Early):**
1. ✅ 40% activation rate
2. ✅ Knowledge graph creates switching costs
3. ✅ 10% free-to-paid conversion
4. ✅ $35 blended CAC achievable
5. ✅ 5% monthly churn sustainable

**Moderate Risk (Monitor Closely):**
- Market size estimates
- Pricing strategy
- Channel performance
- Growth rates

**Lower Risk (Standard Industry Assumptions):**
- API costs
- Competitive pricing
- Operating costs
- Academic market structure

---

*Document Version: 1.0*  
*Last Updated: January 2026*  
*Owner: Ayush Saxena*