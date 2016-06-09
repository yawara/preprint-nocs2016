from pyprimes import factorise

def order_degree(n):
    rtv_o = 1
    rtv_d = 1
    for p, k in factorise(n):
        rtv_o *= p**(2*k)+p**(2*k-1)+p**(2*k-2)
        rtv_d *= p**k+p**(k-1)
    return rtv_o, rtv_d

if __name__ == '__main__':
    for i in range(2, 100):
        o, d = order_degree(i)
        if d <= 23:
            print(*order_degree(i))
