# 📄 Project Summary

## Methodology

The analysis began with cleaning and preprocessing both datasets. Missing values and duplicates were handled, and timestamps were converted to a daily format. The trader dataset was then merged with the sentiment dataset using the date field.

Key features were engineered, including daily PnL per trader, win rate, trade frequency, average trade size, and long/short ratio. These features helped capture both performance and behavioral aspects of traders.

The analysis focused on comparing performance across Fear and Greed market conditions. Additionally, traders were segmented based on activity and consistency to understand differences in behavior and outcomes.

## Insights

The results show that trader performance varies significantly with market sentiment. On Greed days, traders generally achieve higher average PnL and better win rates. Trading activity also increases during these periods.

On Fear days, performance becomes more volatile, indicating higher risk and uncertainty. Traders tend to behave more cautiously, but inconsistent traders often perform poorly.

Segment analysis revealed that consistent traders outperform others across both market conditions, while frequent traders benefit more during favorable market sentiment.

## Strategy Recommendations

Based on these findings, two key strategies are proposed:

1. During Fear days, traders should reduce risk exposure by lowering trade size and frequency, especially those with inconsistent performance.
2. During Greed days, trading activity can be increased selectively for consistent traders, while others should avoid overtrading.

These rules provide a simple yet effective way to adjust trading behavior based on market sentiment.

## Conclusion

This study highlights the importance of combining sentiment analysis with trader behavior to generate actionable insights. It demonstrates how data-driven approaches can improve decision-making in financial markets.
