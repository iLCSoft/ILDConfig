

/** Function to sum up a quantity in a tree.
 *  call as 
 *     LCTuple->Draw("sum()","sum( mcene, Iteration$, nmcp,(mcgst==1) )") ;
 *
 */
float sum(float a=0., int iter=0, int N=0, bool cond=true){ 
  
  static float s = 0. ;
  static float r = 0. ;
  
  if(iter==0 && N==0)
    return r ;
  
  if( cond ) 
    s += a ;
  
  if( iter == N-1 ){
    
    r = s ;
    s = 0; 
    return 1 ;
  } 

  return 0 ;
}


/** Helper function for radius
 */
float r(float x,float y) { return sqrt(x*x+y*y) ; }


/** Helper function for subdet id
 */
int sub(int cellid){

  return ( (unsigned) cellid & 0x0000001f ) ;
}

/** Compute RMS90 - exmaple from R.Brun.
 */
Double_t rms90(TH1 *h) {

  TAxis *axis = h->GetXaxis();
  Int_t nbins = axis->GetNbins();
  Int_t imean = axis->FindBin(h->GetMean());
  //  Double_t entries = 0.9 * h->GetEntries();
  Double_t entries = 0.9 * h->GetSumOfWeights();
  Double_t w = h->GetBinContent(imean);
  Double_t x = h->GetBinCenter(imean);

  Double_t sumw = w;
  Double_t sumwx = w*x;
  Double_t sumwx2 = w*x*x;

  for (Int_t i=1;i<nbins;i++) {
    if ( imean-i > 0) {
      w = h->GetBinContent(imean-i);
      x = h->GetBinCenter(imean-i);
      sumw += w;
      sumwx += w*x;
      sumwx2 += w*x*x;
    }
    if ( imean+i <= nbins) {
      w = h->GetBinContent(imean+i);
      x = h->GetBinCenter(imean+i);
      sumw += w;
      sumwx += w*x;
      sumwx2 += w*x*x;
    }
    //    printf(" i=%d: sumw =%g - entries =%g \n" , i, sumw, entries ) ;
    if (sumw > entries) {
      //      printf(" ---- breaking : sumw =%g - entries =%g,  i=%d" , sumw, entries, i ) ;
      break;
    }
  }
  x = sumwx/sumw;
  Double_t rms2 = TMath::Abs(sumwx2/sumw -x*x); 
  Double_t result = TMath::Sqrt(rms2);

  printf("RMS of central 90%% = %g, RMS total = %g\n, Mean90 = %g , Mean total = %g \n " ,
	 result, h->GetRMS() , x , h->GetMean() );
  
  return result ;
}

