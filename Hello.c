//20240802660
//Viraj Shankar Jadhav
#include <stdio.h>

int main() {
    int n = 7, i, j;
    float weight[7] = {2, 6, 5, 3, 5, 1, 4};
    float profit[7] = {7, 19, 15, 7, 11, 2, 5};
    float ratio[7], temp;
    float capacity = 15;
    float totalProfit = 0.0, remaining = capacity;

    // Step 1: Calculate profit/weight ratio
    for (i = 0; i < n; i++) {
        ratio[i] = profit[i] / weight[i];
    }

    // Step 2: Sort by ratio (descending)
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (ratio[i] < ratio[j]) {
                // swap ratio
                temp = ratio[i];
                ratio[i] = ratio[j];
                ratio[j] = temp;

                // swap weight
                temp = weight[i];
                weight[i] = weight[j];
                weight[j] = temp;

                // swap profit
                temp = profit[i];
                profit[i] = profit[j];
                profit[j] = temp;
            }
        }
    }

    // Step 3: Pick items greedily
    printf("Item\tWeight\tProfit\tTaken\n");
    for (i = 0; i < n; i++) {
        if (weight[i] <= remaining) {
            // take full item
            totalProfit += profit[i];
            remaining -= weight[i];
            printf("%d\t%.2f\t%.2f\t1.00\n", i + 1, weight[i], profit[i]);
        } else {
            // take fractional part
            float fraction = remaining / weight[i];
            totalProfit += profit[i] * fraction;
            printf("%d\t%.2f\t%.2f\t%.2f\n", i + 1, weight[i], profit[i], fraction);
            remaining = 0;
            break;
        }
    }

    printf("\nMaximum Profit = %.2f\n", totalProfit);
    return 0;
}

