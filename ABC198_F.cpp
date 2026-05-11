// LUOGU_RID: 158502209
#include <cstdio>
#define mod(x) (((x)%mod+mod)%mod)
using namespace std;

const int mod = 998244353;

int ans, tmp;
long long n;

int add (int &x, long long y) {return x = (x + y) % mod;}

int qpow (int x, int y)
{
	int res = 1;
	for (; y; y >>= 1)
	{
		if (y & 1) res = (long long) res * x % mod;
		x = (long long) x * x % mod;
	}
	return res;
}

int inv (int x) {return qpow (x, mod - 2);}

int C (long long x, int y)
{
	long long res = 1;
	for (long long i = x; i > x - y; i --)
	{
		res = i % mod * res % mod;
	}
	for (int i = 1; i <= y; i ++)
	{
		res = (long long) res * inv (i) % mod;
	}
	return res;
}

int main ()
{
	scanf ("%lld", &n), n -= 6, ans = C (n + 5, 5);
	tmp = mod (3 * (n + 1) - n / 2 * 4);
	add (ans, (long long) tmp * C (n / 2 + 2, 2));
	add (ans, (n / 4 + 1) % mod * ((n + 1 - n / 4 * 2) % mod) * 6);
	if (n % 2 == 0) add (ans, C (n / 2 + 2, 2) * 6ll);
	if (n % 3 == 0) add (ans, (n / 3 + 1) * 8);
	printf ("%d", (long long) ans * inv (24) % mod);
	return 0;
}