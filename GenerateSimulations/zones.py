import numpy as np

print('=======================================')

class zone:

    def __init__(self, dx, x1, x2, y1, y2, z1, z2, xy, xz, yx, yz, zx, zy):

        self.dxyz = dx
        self.x2 = x2
        self.x1 = x1
        self.y2 = y2
        self.y1 = y1
        self.z2 = z2
        self.z1 = z1

        self.vecx1 = [x1, 0, 0]
        self.vecx2 = [x2, 0, 0]
        self.vecy1 = [0, y1, 0]
        self.vecy2 = [0, y2, 0]
        self.vecz1 = [0, 0, z1]
        self.vecz2 = [0, 0, z2]

        self.out1D_xline_y = xy
        self.out1D_xline_z = xz
        self.out1D_yline_x = yx
        self.out1D_yline_z = yz
        self.out1D_zline_x = zx
        self.out1D_zline_y = zy


        self.vec_xony = [0, self.out1D_xline_y, 0]
        self.vec_xonz = [0, 0, self.out1D_xline_z]
        self.vec_yonx = [self.out1D_yline_x, 0, 0]
        self.vec_yonz = [0, 0, self.out1D_yline_z]
        self.vec_zonx = [self.out1D_zline_x, 0, 0]
        self.vec_zony = [0, self.out1D_zline_y, 0]







# dxyz = 0.003125
# x2 = 3.0625
# x1 = 2.9375
# y2 = 0.5625
# y1 = 0.4375
# z2 = 0.5625
# z1 = 0.4375

# global_nx = 41
# global_ny = 41
# global_nz = 41
# ghost_size = 3.0625



# vecx1 = [x1, 0, 0]
# vecx2 = [x2, 0, 0]
# vecy1 = [0, y1, 0]
# vecy2 = [0, y2, 0]
# vecz1 = [0, 0, z1]
# vecz2 = [0, 0, z2]

# out1D_xline_y=0.5
# out1D_xline_z=0.5

# out1D_yline_x=3.0
# out1D_yline_z=0.5

# out1D_zline_x=3.0
# out1D_zline_y=0.5


# vec_xony = [0, out1D_xline_y, 0]
# vec_xonz = [0, 0, out1D_xline_z]

# vec_yonx = [out1D_yline_x, 0, 0]
# vec_yonz = [0, 0, out1D_yline_z]

# vec_zonx = [out1D_zline_x, 0, 0]
# vec_zony = [0, out1D_zline_y, 0]


    def gridBoxPoints(self):

        print('this is good')
        # All the vectors from origin

        lbp1 = np.add(np.add(self.vecx1, self.vecy1), self.vecz1)
        lbp2 = np.add(np.add(self.vecx1, self.vecy1), self.vecz2)

        ltp1 = np.add(np.add(self.vecx1, self.vecy2), self.vecz1)
        ltp2 = np.add(np.add(self.vecx1, self.vecy2), self.vecz2)


        rbp1 = np.add(np.add(self.vecx2, self.vecy1), self.vecz1)
        rbp2 = np.add(np.add(self.vecx2, self.vecy1), self.vecz2)

        rtp1 = np.add(np.add(self.vecx2, self.vecy2), self.vecz1)
        rtp2 = np.add(np.add(self.vecx2, self.vecy2), self.vecz2)


        # print("left side 4 points")
        # print(lbp1)
        # print(lbp2)
        # print(ltp1)
        # print(ltp2)
        # print('---------')
        # print('right side 4 points')
        # print(rbp1)
        # print(rbp2)
        # print(rtp1)
        # print(rtp2)

        boxpoints = {
            'lbp1': lbp1,
            'lbp2': lbp2,
            'ltp1': ltp1,
            'ltp2': ltp2,
            'rbp1': rbp1,
            'rbp2': rbp2,
            'rtp1': rtp1,
            'rtp2': rtp2
        }

        return boxpoints


    def dataAxis(self):
        data_x_lp = np.add(np.add(self.vecx1, self.vec_xony), self.vec_xonz)
        data_x_rp = np.add(np.add(self.vecx2, self.vec_xony), self.vec_xonz)
        data_x_lp = np.add(data_x_lp, [-0.1, 0, 0])
        data_x_rp = np.add(data_x_rp, [0.1, 0, 0])

        data_y_lp = np.add(np.add(self.vecy1, self.vec_yonx), self.vec_yonz)
        data_y_rp = np.add(np.add(self.vecy2, self.vec_yonx), self.vec_yonz)
        data_y_lp = np.add(data_y_lp, [0, -0.2, 0])
        data_y_rp = np.add(data_y_rp, [0, 0.2, 0])

        data_z_lp = np.add(np.add(self.vecz1, self.vec_zonx), self.vec_zony)
        data_z_rp = np.add(np.add(self.vecz2, self.vec_zonx), self.vec_zony)
        data_z_lp = np.add(data_z_lp, [0, 0, -0.05])
        data_z_rp = np.add(data_z_rp, [0, 0, 0.05])

        print('Data X')
        print(data_x_lp)
        print(data_x_rp)

        print('Data Y')
        print(data_y_lp)
        print(data_y_rp)

        print('Data Z')
        print(data_z_lp)
        print(data_z_rp)

        dataaxis = {
            'data_x_lp': data_x_lp,
            'data_x_rp': data_x_rp,
            'data_y_lp': data_y_lp,
            'data_y_rp': data_y_rp,
            'data_z_lp': data_z_lp,
            'data_z_rp': data_z_rp
        }

        return dataaxis


