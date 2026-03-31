print("**********************************************")
print("........ENERGY SAVING TIP GENERATOR........")
print("**********************************************")

import random

choice='y'
while choice=='y':
  user_input=input("Enter the area you want an energy saving tip for (lighting,heating,kitchen,electronics,general): ")
  if user_input.lower()=='lighting':
     c='y'
     while c=='y':
        tips =["Replace your old incandescent bulbs with energy-efficient LED bulbs.",
          "Always turn off the lights when leaving a room, even for a short time.",
          "Maximize natural daylight by opening curtains and blinds during the day.",
          "Use motion sensors or timers for lights in low-traffic areas like hallways or pantries."]
        r=random.randint(0,3)
        print(tips[r])
        c=input("Do you wish to see more tips(y/n): ")

  elif user_input.lower()=='heating':
       c='y'
       while c=='y':
            tips=["Lower your thermostat by a few degrees (e.g., 2°C) when you're asleep or away to **reduce HVAC electricity use.",
        "Seal air leaks around windows and doors; this reduces the amount of time your **electric heater or AC runs.",
        "Clean or replace your furnace and AC filters monthly; a dirty filter forces the **HVAC fan motor to work harder.",
        "If using central air, close vents in unused rooms to **efficiently direct cooled air."]
            r=random.randint(0,3)
            print(tips[r])
            c=input('Do you wish to see more tips(y/n): ')


  elif user_input.lower()=='kitchen':
       c='y'
       while c=='y':
          tips=["Use the **microwave or toaster oven** instead of the main oven when possible (they consume less electricity).",
        "Keep your refrigerator and freezer settings optimal: **37°F (3°C) for the fridge and 0°F (-18°C)** for the freezer.",
        "Run your dishwasher only when it's full and use the **air-dry setting** instead of the heated dry cycle.",
         "Defrost your freezer regularly, as **ice buildup forces the motor to use more electricity."]
          r=random.randint(0,3)
          print(tips[r])
          c=input('Do you wish to see more tips(y/n): ')


  elif user_input.lower()=='electronics':
      c='y'
      while c=='y':
        tips=["Unplug electronics (like chargers and TVs) that are not in use to stop 'vampire' power draw.",
        "Wash clothes in cold water whenever possible; heating the water is the biggest energy cost.",
        "Take shorter showers and install a low-flow showerhead.",
        "Perform an energy audit to identify where your home is losing the most heat."]
        r=random.randint(0,3)
        print(tips[r])
        c=input('Do you wish to see more tips(y/n): ')

  elif user_input.lower()=='general':
      c='y'
      while c=='y':
         tips=["Unplug electronics (like chargers and TVs) that are not in use to stop 'vampire' power draw.",
          "Wash clothes in cold water whenever possible; heating the water is the biggest energy cost.",
          "Take shorter showers and install a low-flow showerhead.",
          "Perform an energy audit to identify where your home is losing the most heat."]
         r=random.randint(0,3)
         print(tips[r])
         c=input('Do you wish to see more tips(y/n): ')

  else:
      print("Enter the correct area. ")

  choice=input("Do you wish to change the area(y/n): ")
  

  if choice=='n':
    print("---------------------------------------------------------------")
    print("Thank You")
    print("---------------------------------------------------------------")
