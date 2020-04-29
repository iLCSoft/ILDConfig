#include "funs.C"

void draw_etot( const char* FILEN , const char* TupleName="MyLCTuple") {


  std::string pdfFile( std::string( FILEN ) + std::string( "_etot.pdf" ) ) ;

  TFile* f = TFile::Open(FILEN) ;

  TTree* MyLCTuple = (TTree*) f->Get( TupleName ) ;

  TH1F* h0 = new TH1F("h0","total energy [GeV] from MCParticle",120.,60.,120.) ;
  TH1F* h = new TH1F("h","total energy [GeV] from PFOs",120.,60.,120.) ;

  auto* c1 = new TCanvas("C1","Total energy - McTruth vs. PFOs",-5);
  c1->Divide(1,2);
  
  c1->cd(1) ;

  MyLCTuple->Draw("sum()","sum( mcene, Iteration$, nmcp,(mcgst==1) )" ) ;       

  c1->cd(2) ;

  MyLCTuple->Draw("sum()","sum( rcene, Iteration$, nrec, 1)" ) ;       

  //c1->Print( pdfFile.c_str() ) ;

}

 
