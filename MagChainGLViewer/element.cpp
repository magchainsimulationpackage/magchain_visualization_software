/*
 *  element.cpp
 *  MagChainViewer application
 *  Author: Jordi Andreu Segura
 *  e-mail: jandreu@icmab.es
 *  Last Modification: 16/11/2011
 *
 */

#include "element.h"

using namespace std;

void CElement :: Print(){ cerr << "element: " << x << " " << y << " " << z << endl; }

void CFrame :: AddElement(CElement e){ this->element.push_back(e); }
void CFrame :: Print(){	for (unsigned int i=0; i<element.size(); i++) { element[i].Print(); } }
