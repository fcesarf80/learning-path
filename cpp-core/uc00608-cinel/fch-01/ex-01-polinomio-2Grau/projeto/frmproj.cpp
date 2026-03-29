#include "frmproj.h"
using namespace System;
using namespace System::Windows::Forms;
[STAThreadAttribute]
int main(array<String ^> ^argv) {
	Application::EnableVisualStyles();
	Application::SetCompatibleTextRenderingDefault(false);
	projeto::frmproj form;
	Application::Run(%form);
}
