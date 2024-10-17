def combine_signals(signals):
    res=[]
    for i in range(len(signals)-1):
      res.append(signals[i] | signals[i+1])
    return res

# print(combine_signals([8,4,2]))
  