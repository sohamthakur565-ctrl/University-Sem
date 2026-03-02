#include <stdio.h>
int main()
{
    int i, choice, qty;
    int exitFlag = 0;
    const int ITEMS = 6;
    char itemNames[][25] = {
        "Pizza",
        "Burger",
        "Pasta",
        "Coffee",
        "Sandwich",
        "Ice Cream"
    };
    float itemPrices[] = {
        250.0,
        120.0,
        180.0,
        80.0,
        100.0,
        90.0
    };
    int itemQty[6] = {0, 0, 0, 0, 0, 0};
    float subtotal = 0.0;
    float gst = 0.0;
    float discount = 0.0;
    float netAmount = 0.0;
    int customerCount = 1;
    printf("\n<_><_><_><_><_><_><_><_><_><_><_><_><_><_><_>\n");
    printf("        WELCOME TO KK RESTAURANT\n");
    printf("<_><_><_><_><_><_><_><_><_><_><_><_><_><_><_><_>\n");
    while (!exitFlag)
    {
        printf("\n-----------------------------------------------\n");
        printf("Customer No: %d\n", customerCount);
        printf("-----------------------------------------------\n");
        while (1)
        {
            printf("\n<_><_><_><_><_><_> RESTAURANT MENU <_><_><_><_><_><_>\n");
            for (i = 0; i < ITEMS; i++)
            {
                printf("%d. %-15s - Rs %.2f\n",
                       i + 1,
                       itemNames[i],
                       itemPrices[i]);
            }
            printf("7. Show Current Order\n");
            printf("8. Clear Current Order\n");
            printf("0. Generate Final Bill\n");
            printf("===============================================\n");
            printf("Enter your choice: ");
            scanf("%d", &choice);
            if (choice == 0)
            {
                break;
            }
            else if (choice >= 1 && choice <= 6)
            {
                printf("Enter quantity for %s: ",
                       itemNames[choice - 1]);
                scanf("%d", &qty);
                if (qty <= 0)
                {
                    printf("Invalid quantity! Try again.\n");
                }
                else
                {
                    itemQty[choice - 1] += qty;
                    printf("Added %d x %s\n",
                           qty,
                           itemNames[choice - 1]);
                }
            }
            else if (choice == 7)
            {
                printf("\n-------------- CURRENT ORDER ------------------\n");
                for (i = 0; i < ITEMS; i++)
                {
                    if (itemQty[i] > 0)
                    {
                        printf("%-12s : %d\n",
                               itemNames[i],
                               itemQty[i]);
                    }
                }
                printf("-----------------------------------------------\n");
            }
            else if (choice == 8)
            {
                for (i = 0; i < ITEMS; i++)
                {
                    itemQty[i] = 0;
                }
                printf("Order cleared successfully!\n");
            }
            else
            {
                printf("Invalid choice! Try again.\n");
            }
        }
        subtotal = 0.0;
        for (i = 0; i < ITEMS; i++)
        {
            subtotal += itemQty[i] * itemPrices[i];
        }
        if (subtotal == 0)
        {
            printf("\nNo items ordered.\n");
        }
        else
        {
            gst = 0.05f * subtotal;

            if (subtotal >= 1000)
            {
                discount = 0.10f * subtotal;
            }
            else
            {
                discount = 0.0;
            }
            netAmount = subtotal + gst - discount;

            printf("\n\n================ FINAL BILL ===================\n");
            printf("%-5s %-15s %-6s %-10s\n",
                   "No",
                   "Item",
                   "Qty",
                   "Total");
            int srNo = 1;
            for (i = 0; i < ITEMS; i++)
            {
                if (itemQty[i] > 0)
                {
                    float itemTotal =
                        itemQty[i] * itemPrices[i];
                    printf("%-5d %-15s %-6d Rs %-10.2f\n",
                           srNo,
                           itemNames[i],
                           itemQty[i],
                           itemTotal);
                    srNo++;
                }
            }
            printf("-----------------------------------------------\n");
            printf("Subtotal          : Rs %.2f\n", subtotal);
            printf("GST (5%%)          : Rs %.2f\n", gst);
            printf("Discount          : Rs %.2f\n", discount);
            printf("-----------------------------------------------\n");
            printf("Net Amount Payable: Rs %.2f\n", netAmount);
            printf("===============================================\n");
            printf("        THANK YOU! VISIT AGAIN!\n");
            printf("===============================================\n");
        }
        for (i = 0; i < ITEMS; i++)
        {
            itemQty[i] = 0;
        }
        int nextChoice;
        printf("\n1. New Customer");
        printf("\n2. Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &nextChoice);
        if (nextChoice == 1)
        {
            customerCount++;
            continue;
        }
        else
        {
            exitFlag = 1;
        }
    }
    printf("\nSystem Closed Successfully.\n");
    return 0;
}

