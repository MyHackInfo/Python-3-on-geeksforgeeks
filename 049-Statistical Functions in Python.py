'''
    ### Statistical Functions in Python ###
    -Python has the ability to manipulate some statistical data and calculate results of
    -various statistical operations using the file “statistics“, useful in domain of mathematics

    ## Important Average and measure of central location functions:>>
        1. mean() :- This function returns the mean or average of the data passed in its arguments. If passed argument is empty, StatisticsError is raised.
        2. mode() :- This function returns the the number with maximum number of occurrences. If passed argument is empty, StatisticsError is raised.
        3. median() :- This function is used to calculate the median, i.e middle element of data. If passed argument is empty, StatisticsError is raised.
        4. median_low() :- This function returns the median of data in case of odd number of elements, but in case of even number of elements, returns the lower of two middle elements. If passed argument is empty, StatisticsError is raised.
        5. median_high() :- This function returns the median of data in case of odd number of elements, but in case of even number of elements, returns the higher of two middle elements. If passed argument is empty, StatisticsError is raised.
        6. median_grouped() :- This function is used to compute group median, i.e 50th percentile of the data. If passed argument is empty, StatisticsError is raised.
        7. variance() :- This function calculates the variance i.e measure of deviation of data, more the value of variance, more the data values are spread. Sample variance is computed in this function, assuming data is of a part of population. If passed argument is empty, StatisticsError is raised.
        8. pvariance() :- This function computes the variance of the entire population. The data is interpreted as it is of the whole population. If passed argument is empty, StatisticsError is raised.
        9. stdev() :- This function returns the standard deviation ( square root of sample variance ) of the data. If passed argument is empty, StatisticsError is raised.
        10. pstdev() :- This function returns the population standard deviation ( square root of population variance ) of the data. If passed argument is empty, StatisticsError is raised.

'''
# importing statistics to handle statistical operations
import statistics
li = [1, 2, 3, 3, 2, 2, 2, 1,2]
print ("The average of list values is : ",statistics.mean(li))
print ("The maximum occurring element is  : ",statistics.mode(li))
print("The median of list element is :",statistics.median(li))
print("The lower median of list is :",statistics.median_low(li))
print("The highter median of list is :",statistics.median_high(li))
print("The 50th Percentile of data :",statistics.median_grouped(li))
print("The variance of data is :",statistics.variance(li))
print("The population variance of data is:",statistics.pvariance(li))
print("The standard deviation of data is :",statistics.stdev(li))
print("The population standard deviation of data is: ",statistics.pstdev(li))
