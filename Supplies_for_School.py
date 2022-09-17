pen_count = int(input())
markers_count = int(input())
detergent_litres = int(input())
discount_percent = int(input())

price_pen = pen_count * 5.80
markers_price = markers_count * 7.20
detergent_price = detergent_litres * 1.20
all_price = price_pen + markers_price+detergent_price
discount_sum = all_price * (discount_percent / 100)
total_sum = all_price - discount_sum
print(total_sum)
