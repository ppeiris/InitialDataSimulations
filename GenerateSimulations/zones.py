import numpy as np

print('=======================================')

class zone:

    def __init__(self, dx, x1, x2, y1, y2, z1, z2, xy, xz, yx, yz, zx, zy):

        self.dxyz = float(dx)
        self.x2 = float(x2)
        self.x1 = float(x1)
        self.y2 = float(y2)
        self.y1 = float(y1)
        self.z2 = float(z2)
        self.z1 = float(z1)

        self.vecx1 = [self.x1, 0.0, 0.0]
        self.vecx2 = [self.x2, 0.0, 0.0]
        self.vecy1 = [0.0, self.y1, 0.0]
        self.vecy2 = [0.0, self.y2, 0.0]
        self.vecz1 = [0.0, 0.0, self.z1]
        self.vecz2 = [0.0, 0.0, self.z2]

        self.out1D_xline_y = float(xy)
        self.out1D_xline_z = float(xz)
        self.out1D_yline_x = float(yx)
        self.out1D_yline_z = float(yz)
        self.out1D_zline_x = float(zx)
        self.out1D_zline_y = float(zy)


        self.vec_xony = [0.0, self.out1D_xline_y, 0.0]
        self.vec_xonz = [0.0, 0.0, self.out1D_xline_z]
        self.vec_yonx = [self.out1D_yline_x, 0.0, 0.0]
        self.vec_yonz = [0.0, 0.0, self.out1D_yline_z]
        self.vec_zonx = [self.out1D_zline_x, 0.0, 0.0]
        self.vec_zony = [0.0, self.out1D_zline_y, 0.0]


    def gridBoxPoints(self):

        # All the vectors from origin

        lbp1 = np.add(np.add(self.vecx1, self.vecy1), self.vecz1)
        lbp2 = np.add(np.add(self.vecx1, self.vecy1), self.vecz2)

        ltp1 = np.add(np.add(self.vecx1, self.vecy2), self.vecz1)
        ltp2 = np.add(np.add(self.vecx1, self.vecy2), self.vecz2)

        rbp1 = np.add(np.add(self.vecx2, self.vecy1), self.vecz1)
        rbp2 = np.add(np.add(self.vecx2, self.vecy1), self.vecz2)

        rtp1 = np.add(np.add(self.vecx2, self.vecy2), self.vecz1)
        rtp2 = np.add(np.add(self.vecx2, self.vecy2), self.vecz2)

        boxpoints = {
            'lbpone': lbp1,
            'lbptwo': lbp2,
            'ltpone': ltp1,
            'ltptwo': ltp2,
            'rbpone': rbp1,
            'rbptwo': rbp2,
            'rtpone': rtp1,
            'rtptwo': rtp2
        }


        return boxpoints


    def dataAxis(self):
        data_x_lp = np.add(np.add(self.vecx1, self.vec_xony), self.vec_xonz)
        data_x_rp = np.add(np.add(self.vecx2, self.vec_xony), self.vec_xonz)
        data_x_lp = np.add(data_x_lp, [-0.05, 0, 0])
        data_x_rp = np.add(data_x_rp, [0.05, 0, 0])

        data_y_lp = np.add(np.add(self.vecy1, self.vec_yonx), self.vec_yonz)
        data_y_rp = np.add(np.add(self.vecy2, self.vec_yonx), self.vec_yonz)
        data_y_lp = np.add(data_y_lp, [0, -0.02, 0])
        data_y_rp = np.add(data_y_rp, [0, 0.02, 0])

        data_z_lp = np.add(np.add(self.vecz1, self.vec_zonx), self.vec_zony)
        data_z_rp = np.add(np.add(self.vecz2, self.vec_zonx), self.vec_zony)
        data_z_lp = np.add(data_z_lp, [0, 0, -0.02])
        data_z_rp = np.add(data_z_rp, [0, 0, 0.02])

        dataaxis = {
            'dataxlp': data_x_lp,
            'dataxrp': data_x_rp,
            'dataylp': data_y_lp,
            'datayrp': data_y_rp,
            'datazlp': data_z_lp,
            'datazrp': data_z_rp
        }


        return dataaxis


