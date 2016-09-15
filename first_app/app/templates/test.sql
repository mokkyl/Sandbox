SELECT
        SUM(offer_rewards.amount)
FROM public.fact_completed_offer_engagements as  fact_completed_offer_engagements
INNER JOIN public.offer_rewards as offer_rewards ON offer_rewards.id = fact_completed_offer_engagements.offer_reward_id

WHERE
        verified is not null
        AND fact_completed_offer_engagements.offer_id in 
                        (
                                SELECT DISTINCT
                                       offers.id 
                                FROM public.offers as offers
                                INNER JOIN public.campaigns as campaigns ON campaigns.id = offers.campaign_id
                              --  INNER JOIN public.contracts as contracts ON contracts.id = campaigns.contract_id
                               -- INNER JOIN  public.contract_cpg_accounts as contract_cpg_accounts ON contract_cpg_accounts.contract_id = contracts.id
                                WHERE
                                        campaigns.category_second in ('Beer','Wine','Spirits')
                               --         AND cpg_account_id = 307
                        )
