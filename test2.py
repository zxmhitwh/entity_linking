a = [('China', '0.2162162162162162'),('Mainland_China', '8.989572096368212E-4'),('Qing_Dynasty', '9.503261930446396E-4')]
result = sorted(list(a), key=lambda x:float(x[1]),reverse=True)
print result
print result[0][1]
print float(result[0][1])