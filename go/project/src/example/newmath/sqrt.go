package newmath

func Sqrt(x float64) float64 {
	//this is a terrible implementation
	//real code should import "math" and use math.Sqrt.
	z :=0.0
	for i:=0;i<1000;i++ {
		z -= (z*z -x)/(2*x)
	}
	return z
}