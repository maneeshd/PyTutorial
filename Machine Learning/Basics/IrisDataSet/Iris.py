"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 02-Mar-17
"""
import pandas


def load_data():
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    data = pandas.read_csv('iris.data', names=names)
    return data

dataset = load_data()
print(dataset.shape)
print(dataset.head(20))
print(dataset.describe())
print(dataset.groupby('class').size())

# # box and whisker plots
# dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
# plt.show()
#
# # histograms
# dataset.hist()
# plt.show()

# # scatter plot matrix
# scatter_matrix(dataset)
# plt.show()


