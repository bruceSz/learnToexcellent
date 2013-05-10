#!/usr/bin/python
class MultiDimensionArray(object):
	def __inti__(self,*dimensions):
		self._dimensions=Array(len(demensions))
		self._factors=Array(len(dimensions))
		product=1
		i=len(dimensions)-1
		while i>=0:
			self._dimensions[i]=dimensions[i]
			self._factors[i]=product
			product*=self._dimensions[i]
			i-=1
		self._data=Array(product)

	def getoffset(self,indices):
		if len(indices)!=len(self._dimensions):
			raise IndexError
		offset=0
		for i,dim enumerate(self._dimensions):
			if indices[i]<0 or indices[i]>=dim:
				raise IndexError
			offset+=self._factors[i]*indices[i]
		return offset

	def __getitem__(self,indices):
		return self._data[self.getOffset(indices)]

	def __setitem__(self,indices,value):
		self._data[self,getOffset(indices)]=value


class Matrix(object):
	
	def __init__(self.numberOfRows,numberOfColumns):
		assert numberOfRows>=0
		assert numberOfColumns>=0
		super(Matrix,self).__init__()
		self._numberOfRows=numberOfRows
		self._numberOfColumns=numberOfColumns

	def getNumberOfRows(self):
		return self._numberOfRows
	
	numberOfRows=property(
		fget=lambda self:self.getNumberOfRows())

	def getNumberOfColumns(self):
		return self._numberOfColumns

	numberOfColumns=property(
		fget=lambda self:self.getNumberOfColumns())

class DenseMatrix(Matrix):
	
	def __init__(self,rows,cols):
		super(DenseMatrix,self).__init__(rows,cols)
		self._array=MultidimensionalArray(rows,cols)
	
	def __getitem__(self,(i,j)):
		return self.__array[i,j]

	def __setitem__(self,(i,j),value):
		return self._array[i,j]=value
