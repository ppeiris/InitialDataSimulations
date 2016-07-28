SHELL=/bin/sh

include $(HOME_LORENE)/local_settings

LIB = -L$(HOME_LORENE)/Lib -llorene -llorenef77 $(LIB_CXX) $(LIB_GSL) $(LIB_LAPACK)

.SUFFIXES : .o .C

SRC1 = manybh.C manybh_equations.C
OBJ1 = $(SRC1:.C=.o)
EXE1 = manybh

$(EXE1): $(OBJ1)
	$(CXX) -o $@ $(OBJ1) $(CXXFLAGS) $(LIB) 

.C.o:
	$(CXX)  -c $(INC) $(CXXFLAGS) $<

uninstall:
	rm -f $(OBJ1)
	rm -f $(EXE1)


