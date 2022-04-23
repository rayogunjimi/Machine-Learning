def model1(lxry, yr, mpg, hp):
    return 1000*lxry+5*yr+100*mpg+150*hp-15000

def model2(lxry, yr, mpg, hp):
    return 900*lxry+10*yr+80*mpg+120*hp-10000

def testmodel(lxry, yr, mpg, hp):
    return 1000*lxry+5*yr+100*mpg+150*hp-14000

def square_difference(actual, prediction):
    return (prediction-actual)**2

mdl = ["Acura MDX", "Honda Acord", "Honda Civic", "Honda Civic", "Nissan Altima", "Acura MDX", "Lexus RX350", "Toyota Prius", "Toyota Prius"]
lxry = [1, 0, 0, 0, 0, 1, 1, 0, 0]
yr = [2017, 2017, 2012, 2016, 2016, 2015, 2015, 2014, 2013]
mpg = [20, 25, 23, 24, 30, 18, 21, 45, 40]
hp = [290, 190, 160, 170, 180, 280, 270, 120, 120]
price = [50000, 25000, 10000, 18000, 25000, 38000, 40000, 28000, 24000]


def main():
    sum_square_diff_model1 = 0
    sum_square_diff_model2 = 0
    sum_square_diff_testmodel = 0
    for i in range(len(mdl)):
        sum_square_diff_model1 += square_difference(price[i], model1(lxry[i], yr[i], mpg[i], hp[i]))
        sum_square_diff_model2 += square_difference(price[i], model2(lxry[i], yr[i], mpg[i], hp[i]))
        sum_square_diff_testmodel += square_difference(price[i], testmodel(lxry[i], yr[i], mpg[i], hp[i]))

    print("model 1:", sum_square_diff_model1/(len(mdl)*2))
    print("model 2:", sum_square_diff_model2/(len(mdl)*2))
    print("testmodel:", sum_square_diff_testmodel/(len(mdl)*2))

# based on the cost function value results model 1 is better becasue 21555345.833333332 (model 1) < 52934494.44444445 (model 2)
# one model that performs better than both, could be: h_theta(x) = 1000*x_1 + 5*x_2 + 100*x_3 + 150*x_4 - 14000
#this model has a cost function value of 21197012.5 < 21555345.833333332 (model 1) < 52934494.44444445 (model 2)

if __name__ == '__main__':
    main()