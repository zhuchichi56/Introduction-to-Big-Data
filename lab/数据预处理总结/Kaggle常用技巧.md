

##### 1.按照某种要求更新某一列：

```python
@jit(nopython=True)
def change(x):
    if(x<=35) :return 'low'
    elif(x<=150): return 'polluting '
    else:return 'very high'

text['pm2.5'] =text.apply(lambda x: change(x['pm2.5']),axis=1)

```



##### 2.norm types 转化成 float type

```python
#方法1 
element = text['pm2.5'].unique()
dictionary = dict(zip(element,range(0,len(element)))) #反转
text['pm2.5'] = text.apply(lambda x:dictionary[x['pm2.5']],axis=1)
```



##### 3.onehot_encoding ： 直接

```python
# one-hot encoding
text['cbwd'].unique()
df = text.join(pd.get_dummies(text['cbwd']).astype('float'))
del df['cbwd']
```

```python
to_beencoder = text['cbwd'].to_numpy()
from sklearn.preprocessing import  OneHotEncoder

encoder = OneHotEncoder(sparse=False).fit(to_beencoder.reshape(-1,1))
def encoding(data):
    return encoder.transform(data.reshape(-1,1))
def decoding(one_hot_data):
    return encoder.inverse_transform(one_hot_data)


b  = encoding(text['cbwd'].to_numpy())
print(b)
b =pd.Series(np.squeeze(b))
a =decoding(encoding(text['cbwd'].to_numpy()))
a =pd.Series(np.squeeze(a) )
```



##### 4.type 的统一

```python
text.dtypes
sth.astype('float')
```



##### 5.转化日期为index

```python
import datetime
text['time'] = text.apply(lambda x : datetime.datetime(year=x['year'], month=x['month'], day=x['day'], hour=x['hour']), axis=1)
#drop 多列的方法
text.drop(columns=['year', 'month', 'day', 'hour', 'No'], inplace=True)
df = text.set_index('time')
df.head()
```



##### 6.分离数据集

```python
y = data.pop('price')
```



##### 7.inplace = True 操纵地址:

```python
new_text = text  #指向了同一块地址
new_text.dropna(inplace = True)
text
```

此时都发生了改变

```python
new_text = text.copy() #创建了新的对象，并非同一块地址
new_text.dropna(inplace = True)
text #不发生改变
```





##### 8.change order

```python
df_id = df.id
df = df.drop('id',axis=1)
df.insert(0,'id',df_id)
```



##### 9.inner join

```python
intersected_df = pd.merge(Train_set['No'],Test_set['No'], how='inner')
Train_set['No']
```





