def delete_nth(order,max_e):
    for elem in order:
        ctr = order.count(elem)
        if(ctr > max_e):
              order.reverse()
              for num in range(ctr - max_e):
                    del order[order.index(elem)]
              order.reverse()
    return order
                 
            
