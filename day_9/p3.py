import numpy as np

while True:
    # 1. Create a 2x3 array of random numbers
    ranarr = np.random.rand(2, 3)
    print("\nRandom array (ranarr):\n", ranarr)

    # 2. Create another 2x3 array of ones
    onearr = np.ones((2, 3))
    print("\nArray of ones (onearr):\n", onearr)

    # 3. Generate boolarr with elements > 0.5
    boolarr = ranarr > 0.5
    print("\nBoolean array (boolarr):\n", boolarr)
    print("Shape of boolarr:", boolarr.shape)

    # 4. Boolean index onearr using boolarr
    newarr = onearr[boolarr]
    print("\nNew array (newarr):\n", newarr)
    print("Shape of newarr:", newarr.shape)

    # 5. Ask user if they want to run again
    choice = input("\nRun again? (y/n): ").lower()
    if choice != 'y':
        break
