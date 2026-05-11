package main
import "net"

// Get localIP list from the network accesing to the site



// GetOutboundIP returns the outbound IP address of this machine.
func GetOutboundIP() (string, error) {
	// net.Dial で一度外部にアクセスして、使用したネットワークカードの
	// 情報を取得する。アクセス先は、存在する IP アドレスであれば
	// 8.8.8.8 でなくても構わない。
	conn, err := net.Dial("udp", "8.8.8.8:80")
	if err != nil {
		return "", err
	}

	defer conn.Close()

	// 使用しているネットワークカードのローカル IP を取得
	localAddr := conn.LocalAddr().(*net.UDPAddr)

	return localAddr.IP.String(), nil
}

func main() {



}
1at0p
