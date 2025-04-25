# Cost Variables
ground_flat_charge = 20.0
ground_charge_total = 0.0
premium_ground_flat_charge = 125.0
drone_charge_total = 0.0

# Enter weight here
weight = 41.5

# Calculate and Return Ground Shipping
if weight >= 0.0 and weight < 2.0:
  ground_charge_total = weight * 1.5 + ground_flat_charge
  drone_charge_total = weight * 4.5
elif weight > 2.0 and weight <= 6.0:
  ground_charge_total = weight * 3.0 + ground_flat_charge
  drone_charge_total = weight * 9.0
elif weight > 6.0 and weight <= 10.0:
  ground_charge_total = weight * 4.0 + ground_flat_charge
  drone_charge_total = weight * 12.0
elif weight > 10.0:
  ground_charge_total = weight * 4.75 + ground_flat_charge
  drone_charge_total = weight * 14.25
else:
  print("Sorry, we only ship items with mass")
  exit()

# Print Results
print(f"Ground Shipping: USD${ground_charge_total:.2f}")
print(f"Drone Shipping: USD${drone_charge_total:.2f}")
print(f"Premium Shipping: USD${premium_ground_flat_charge:.2f}")

# Determine and Print cheapest method
cheapest_method = min(ground_charge_total,drone_charge_total,premium_ground_flat_charge)
if cheapest_method == ground_charge_total:
  print(f"\nLet's save you some bucks by using Standard Ground for {ground_charge_total:.2f}")
elif cheapest_method == drone_charge_total:
  print(f"\nLet's save you some bucks by using Drone Shipping for {drone_charge_total:.2f}")
elif cheapest_method == premium_ground_flat_charge:
  print(f"\nLet's save you some bucks by using Premium Ground for {premium_ground_flat_charge:.2f}")
else:
  print("Error in calculating cheapest method encountered")