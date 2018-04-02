# coding: utf-8
from PIL import Image
import numpy as np
from random import sample


class Merge(object):
    """合并QQ头像为矩阵"""

    def __init__(self, pic_mat):
        """
        初始化参数
        Parameters
        ----------
        pic_mat: array
            许多图片组合组成的矩阵
        
        Returns
        -------
            None
        """
        self.pic_mat = pic_mat

    def __merge_row(self, col_lst):
        """
        合并部分图片到一列
        Parameters
        ----------
        col_lst array: 
            每一列图片矩阵的列表
        
        Returns
        -------
        array    
            basemat: 将列表中的图片拼接成一列
        """
        # 转换图片为numpy数组，按列拼接图片
        basemat = col_lst[0]
        for file in col_lst[1:]:
            basemat = np.concatenate((basemat, file), axis=0)
        return basemat

    def __merge_col(self, picmat_lst, n):
        """
        合并列图片组成完整图片
        Parameters
        ----------
        picmat_lst　array:
            所有图片矩阵的列表
        n int: 
            n行n列

        Returns:
        --------
        array    
            row_lst: 所有图片拼接完成后
        """
        # 总共有n行, n列
        row_lst = self.__merge_row(picmat_lst[0:n])
        for i in range(1, n):
            temp_mat = self.__merge_row(picmat_lst[n * i:n * (i + 1)])
            row_lst = np.concatenate((row_lst, temp_mat), axis=1)

        return row_lst

    def merge_pic(self, picname):
        """
        合并图片主函数
        Parameters
        ----------
        picmat_lst array: 
            所有图片矩阵的列表

        Returns:
        --------
            None
        直接保存图片到本地
        """
        # 如果图片数量不符合n*n，则报错
        # assert len(picmat_lst) == (int(len(picmat_lst)**0.5))**2

        # 提取能够最大组成n*n的图片数量
        for i in range(30)[::-1]:
            if i**2 < len(self.pic_mat):
                n = i
                break

        print("组成{}x{}的图片".format(str(n), str(n)))
        print("由{}张图片组成".format(n * n))
        # 随机取n*n张图片
        pic_mat = self.__merge_col(sample(self.pic_mat, n * n), n)
        # 顺序取n*n张
        # pic_mat = self.__merge_col(self.pic_mat[:n * n], n)

        # 数组转图片
        report_img = Image.fromarray(pic_mat)
        report_img.save(picname)
