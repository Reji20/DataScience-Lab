#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv("C:\\Users\Administrator\\Desktop\\iris.csv")
print(df)


# In[2]:


import pandas as pd
df=pd.read_csv("C:\\Users\Administrator\\Desktop\\iris.csv")
print(df.head)


# In[4]:


import pandas as pd
df=pd.read_csv("C:\\Users\Administrator\\Desktop\\iris.csv")
print(df.info())


# In[5]:


import pandas as pd
data=pd.read_csv("C:\\Users\Administrator\\Desktop\\iris.csv")
print(data.head(10))


# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C:\\Users\Administrator\\Desktop\\iris.csv")
print(data.head(10))


# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:\\Users\Administrator\\Desktop\\iris.csv")
plt.plot(data.id,data["sepal.length"],"r--")


# In[15]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:\\Users\Administrator\\Desktop\\iris.csv")
data.plot(kind="scatter",x='sepal.length',y='petal.length')
plt.grid()


# In[18]:


import matplotlib.pyplot as plt
from sklearn import datasets
bins=20
iris=datasets.load_iris()
x_iris =iris.data
x_sepal=x_iris[:,0]
plt.hist(x_sepal,bins)
plt.title("Histogram")
plt.xlabel(iris.feature_names[0])
plt.ylabel("Frequency")
plt.show


# In[ ]:





# In[ ]:




