import pandas as pd


def order_status(df):
    """Gets the shipment status of every order."""
    out = pd.DataFrame([{}])
    # Get all the unique orders
    orders = pd.unique(df.order_number)
    for order in orders:
        # Classify orders based on the shipment status of the individual items on it
        if (df[df.order_number == order].status == 'PENDING').any():
            temp = {'order_number': order, 'status': 'PENDING'}
        elif (df[df.order_number == order].status == 'CANCELLED').all():
            temp = {'order_number': order, 'status': 'CANCELLED'}
        else:
            temp = {'order_number': order, 'status': 'SHIPPED'}
        out = out.append(pd.DataFrame([temp]))
    out.reset_index(drop=True, inplace=True)
    out.drop(0, inplace=True)
    return out


input = pd.DataFrame({
    'order_number': [
        'ORD_1567', 'ORD_1567', 'ORD_1567', 'ORD_1234', 'ORD_1234',
        'ORD_1234', 'ORD_9834', 'ORD_9834', 'ORD_7654', 'ORD_7654'
    ],
    'item_name': [
        'LAPTOP', 'MOUSE', 'KEYBOARD', 'GAME', 'BOOK',
        'BOOK', 'SHIRT', 'PANTS', 'TV', 'DVD'
    ],
    'status': [
        'SHIPPED', 'SHIPPED', 'PENDING', 'SHIPPED', 'CANCELLED',
        'CANCELLED', 'SHIPPED', 'CANCELLED', 'CANCELLED', 'CANCELLED'
    ]
})

print(order_status(input))
