def create_batches(items, batch_size):
    if batch_size <= 0:
        raise ValueError(f"cannot create sub batch with size 0 or less than 0")
    new_list = []
    for i in range(0, len(items), batch_size):
        inner_list = items[i:i+batch_size]
        new_list.append(inner_list)
    return new_list

result = create_batches(items = [1, 2, 3, 4, 5, 6, 7], batch_size = 3)
print(result)

