class Tenseur ;
class Tenseur_sym ;
class Map_et ;

class BHpunc {
  
 protected:

  // Mapping
  Map_et& mp ;
  
  // u
  Tenseur u ;
  Tenseur u1 ;
  Tenseur u2 ;
  Tenseur alpha ;
  Tenseur beta ;

  Tenseur rhsval ;

  Tenseur kxxp ;
  Tenseur kxyp ;
  Tenseur kxzp ;
  Tenseur kyyp ;
  Tenseur kyzp ;
  Tenseur kzzp ;
  Tenseur kxxs ;
  Tenseur kxys ;
  Tenseur kxzs ;
  Tenseur kyys ;
  Tenseur kyzs ;
  Tenseur kzzs ;
  
  // Sources at the previous step
  Tenseur so_jm1_u ;

 public:
  // Constructors
  BHpunc (Map_et& mapping);
  
  // Destructor
  ~BHpunc() ;

  int twostars;
  double xbh[3];
  double pbh[3];
  double sbh[3];
  double mbh;

 public:

  void sauve (FILE*) const ;

  void operator= (const BHpunc&) ;
  
  const Map_et& get_mp() const {return mp ;};

 public:

  Tenseur& set_alpha() {return alpha;} ;
  Tenseur& set_beta() {return beta;} ;
  Tenseur& set_u() {return u;} ;
  Tenseur& set_u1() {return u1;} ;
  Tenseur& set_u2() {return u2;} ;
  Tenseur& set_rhsval() {return rhsval;} ;

  Tenseur& set_kxxp() {return kxxp;} ;
  Tenseur& set_kxyp() {return kxyp;} ;
  Tenseur& set_kxzp() {return kxzp;} ;
  Tenseur& set_kyyp() {return kyyp;} ;
  Tenseur& set_kyzp() {return kyzp;} ;
  Tenseur& set_kzzp() {return kzzp;} ;
  Tenseur& set_kxxs() {return kxxs;} ;
  Tenseur& set_kxys() {return kxys;} ;
  Tenseur& set_kxzs() {return kxzs;} ;
  Tenseur& set_kyys() {return kyys;} ;
  Tenseur& set_kyzs() {return kyzs;} ;
  Tenseur& set_kzzs() {return kzzs;} ;


  void export_data();

  void solve_config (double precis, int ite_max,
			  double relax, int ite_poisson_max) ;
  void solve_equation (double, int) ;

};

class Many_BH {
  
 public:

  int nbh;
  
  double* xbhvec;

 protected:
  
  Map_et** maparray;

  // two components
  BHpunc** bhpuncarray ;
  
 public:
  // Constructors
  Many_BH (int & nbh, Map_et** maparray, BHpunc** bhpuncarray, double* xbhvec) ;
  
  // Destructor
  ~Many_BH() ;

 public:

  void sauve (FILE*) const ;

  void operator= (const Many_BH&) ;
  
 public:

  BHpunc* set_bh(int n) {return bhpuncarray[n];} ;

  void calc_us() ;

  void solve_config (double precis, int ite_max,
			  double relax, int ite_poisson_max) ;

 // void export_data();
  void export_data(char *fname , char *fGridInput_name);
};
