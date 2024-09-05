def greet_user(first_name,last_name):
    print(f'Hello {first_name}')


greet_user(last_name="Tanveer",first_name="afser")
def calc_cost(total,shipping,discount):
    sum = total +shipping;
    sum=sum-sum*0.1
    print(sum)

calc_cost(total=50,shipping=5,discount=0.1)