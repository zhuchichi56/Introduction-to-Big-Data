### 一.Column

##### 1.rename 





##### 2.change order

```python
df_id = df.id
df = df.drop('id',axis=1)
df.insert(0,'id',df_id)
```



##### 3.inner join

```python
intersected_df = pd.merge(Train_set['No'],Test_set['No'], how='inner')
Train_set['No']
```



