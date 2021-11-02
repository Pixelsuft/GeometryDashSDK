#define WIN32_LEAN_AND_MEAN
#define CONSOLE


#include <windows.h>
#include <cocos2d.h>
#include <MinHook.h>
#include <queue>
#include <mutex>
#include <fstream>
#include <sstream>


using namespace std;
using namespace cocos2d;


DWORD base;
DWORD cocos_base;
HANDLE pHandle;
int pid;



DWORD WINAPI my_thread(void* hModule) {
#ifdef CONSOLE
    AllocConsole();
    std::ofstream conout("CONOUT$", std::ios::out);
    std::ifstream conin("CONIN$", std::ios::in);
    std::cout.rdbuf(conout.rdbuf());
    std::cin.rdbuf(conin.rdbuf());
#endif

    base = (DWORD)GetModuleHandleW(0);
    cocos_base = (DWORD)GetModuleHandleW(L"cocos2d.dll");
    pHandle = GetCurrentProcess();
    pid = GetCurrentProcessId();

    MH_Initialize();
	
	// Hooks there
	
    MH_EnableHook(MH_ALL_HOOKS);

    return 0;
}

BOOL APIENTRY DllMain(HMODULE module, DWORD reason, LPVOID) {
    if (reason == DLL_PROCESS_ATTACH) {
        DisableThreadLibraryCalls(module);
        CreateThread(0, 0, my_thread, module, 0, 0);
    }
    return TRUE;
}
