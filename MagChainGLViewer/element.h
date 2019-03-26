/*
 *  element.h
 *  MagChainViewer application
 *  Author: Jordi Andreu Segura
 *  e-mail: jandreu@icmab.es
 *  Last Modification: 16/11/2011
 *
 */

#include<iostream>
#include <vector>

using namespace std;


class CElement{

public:

	float x;
	float y;
	float z;

	float length;
	float diameter;

	CElement(float xx, float yy, float zz, float ll, float dd) : x(xx), y(yy), z(zz), length(ll), diameter(dd){}
	~CElement(){};
	
	void Print();
	
};


class CFrame{

public:

	int id;
	vector <CElement> element;

	CFrame(int i) : id(i) {}
	~CFrame(){ element.clear();	}
	
	void AddElement(CElement e);
	void Print();

};