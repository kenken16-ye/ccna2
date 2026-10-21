
<!-- Your monitor number = #$34T# -->

## ⛅ Warm Up for Day 3.

<br>

### 🔧 Configure the following:
  - Switch (__CoreTAAS__ & __CoreBABA__)
  - Voice Gateway/Call Manager (__CUCM - Cisco Unified Call Manager__)
  - Router (__EDGE__)

<br>

| CIDR | SUBNET MASK     | RIVAN    | WILDCARD     |
| ---  | ---             | ---      | ---          |
| /18  |                 |          |              |
|      | 255.255.255.224 |          |              |
|      |                 | 2nd, 4i  |              |
|      |                 |          | 0.0.0.3      |

<br>

| BitLen |       |
| ---    | ---   |
| 42     |       |
| 1800   |       |
| 365    |       |
| 980    |       |
| 112    |       |

<br>

### Design a network for teleperformance.com with 720 users. Use the available IP address space 10.42.0.0 /16

> C:

<br> 

> S:

<br>

> I:  

<br>

| teleperformance.com     | IPv4  |
| ---                     | ---   |
| Network                 |       |
| First Valid             |       |
| Last Valid              |       |
| Last IP/Broadcast       |       |
| ---                     | ---   |
| NOT teleperformance.com |       |

&nbsp;
---
&nbsp;

### Configure 32 offices for teleperformance.com using the available network address 192.168.0.0/16. Determine the first & last valid IP of the 4th office

> C:

<br> 

> A:

<br>

> I:  

<br>

| teleperformance.com     | IPv4  |
| ---                     | ---   |
| 4th Office: Network     |       |
| First Valid             |       |
| Last Valid              |       |
| Last IP/Broadcast       |       |
| ---                     | ---   |
| NOT 4th Office          |       |


<br>
<br>

---
&nbsp;


# 🏢 Establish Network Connectivity

<br>

## Job Interview Questions for L1/L2 NOC-MSP postions.
### Interpret the components of a Routing Table.
A routing table is a database, also known as a RIB (Routing Information Base), used by network devices to determine the most efficient path for data packets as they travel across a network.
- Linux: `netstat -rn`
- Windows: `route print`
- Cisco: `show ip interface brief`

<br>
<br>

---
&nbsp;

## Master Routing using RIVAN RSTHAYUP LAB
~~~
Login: root
Pass: C1sc0123

Lab: RSTvX

Devices
Secret: pass
~~~

<br>
<br>

---
&nbsp;


### 🎯 Exercise 01: Review on DHCP & IP addressing.
What are the steps to configure DHCP?  
1. Exclude IP addresses
2. Create DHCP pool
    - Network
    - Default-Router
    - Domain-Name
    - DNS-Server

3. Assign DHCP clients

<br>

### DHCP Process
| Acronym | Full Form   | Traffic Type |
| ---     | ---         | ---          |
| D       | Discover    | Broadcast    |
| O       | Offer       | Unicast      |
| R       | Request     | Broadcast    |
| A       | Acknowledge | Unicast      |

<br>

### DHCP Loadbalancing
~~~
!@C1
conf t
 ip dhcp excluded-address 10.2.1.1 10.2.1.100
 ip dhcp excluded-address 10.2.1.199 10.2.1.254
 ip dhcp pool MGMTPOOL.COM
  network 10.2.1.0 255.255.255.0
  default-router 10.2.1.254
  domain-name MGMTPOOL.COM
  dns-server 10.2.1.133
  end
~~~

<br>

~~~
!@C2
conf t
 ip dhcp excluded-address 10.2.1.1 10.2.1.200
 ip dhcp pool MGMTPOOL.COM
  network 10.2.1.0 255.255.255.0
  default-router 10.2.1.254
  domain-name MGMTPOOL.COM
  dns-server 10.2.1.133
  end
~~~


<br>
<br>

---
&nbsp;


### VLAN Assignment - Place PCs (P1, P2) on VLAN 10

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

---
&nbsp;


### DHCP Clients - Configure P1 & P2 to be a DHCP client.

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

---
&nbsp;


What IP addresses did P1 & P2 get?

~~~
!@P1 & P2
show ip int brief | ex una
~~~


<br>
<br>

---
&nbsp;


### Static IP addressing.

~~~
!@P1
conf t
 int e0/0
  no shut
  ip add 10.2.1.101 255.255.255.0
  end
show ip int brief | ex una
~~~

<br>

~~~
!@P2
conf t
 int e1/0
  no shut
  ip add 10.2.1.102 255.255.255.0
  end
show ip int brief | ex una
~~~

<br>

~~~
!@S1
conf t
 int e1/0
  ip add 192.168.1.133 255.255.255.224
  no shut
  end
show ip int brief | ex una
~~~

<br>

~~~
!@S2
conf t
 int e1/0
  ip add 10.2.2.133 255.255.255.0
  no shut
  end
show ip int brief | ex una
~~~


<br>
<br>

---
&nbsp;


### VLAN Assignment

~~~
!@C1
conf t
 int e1/0
  switchport mode access
  switchport access vlan 100
  end
show vlan brief
~~~

<br>

~~~
!@C2
conf t
 int e1/0
  switchport mode access
  switchport access vlan 20
  end
show vlan brief
~~~

<br>

~~~
!@A1
conf t
 int e0/0
  switchport mode access
  switchport access vlan 10
  end
show vlan brief
~~~

<br>

~~~
!@A2
conf t
 int e1/0
  switchport mode access
  switchport access vlan 10
  end
show vlan brief
~~~


<br>
<br>

---
&nbsp;


## 🔀 Static & Default Routing
*What is the normal behavior for network connectivity?*

<br>

~~~
!@R1
ping 10.1.1.2
vs
ping 10.1.1.5
~~~

Is the result normal? 

<br>

### Static Routing Configuration
Syntax:
`ip route [Destination IP]  [Network/Host Mask]  [Exit Interface / Nex-hop]`

<br>

What is a next-hop?

<br>

~~~
!@cmd
tracert 8.8.8.8

Tracing route to 8.8.8.8 over a maximum of 30 hops
  1     2 ms     1 ms     1 ms  192.168.1.1
  2     5 ms     6 ms     5 ms  100.83.0.1
  3     6 ms    11 ms     7 ms  122.2.203.6
  4    12 ms     6 ms     7 ms  210.213.130.15
  5    66 ms    62 ms    49 ms  142.250.175.196
  6     6 ms     6 ms     6 ms  142.251.251.47
  7     8 ms     5 ms     7 ms  142.250.58.243
  8     6 ms    10 ms    10 ms  8.8.8.8
~~~

<br>

Next-hop = 

<br>

~~~
!@R1
conf t
 ip route 10.1.1.5 255.255.255.255 10.1.1.2
 end
ping 10.1.1.5
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 03: Configure a static route on R2 destined for R3's e1/2 interface.
~~~
!@R2
conf t
 ip route __.__.__.__  __.__.__.__  __.__.__.__
 end
~~~

<br>
<br>
<br>
<br>
<br>
<br>

---
&nbsp;


### 🎯 Exercise 04: Configure a static route on R1 destined for R3's e1/1 interface.
~~~
!@R1
conf t
 ip route __.__.__.__  __.__.__.__  __.__.__.__
 end
~~~

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

---
&nbsp;


### Host Route vs Network Route

### 🎯 Exercise 05: Review. Find the network of the following IP addresses:
| Network          | Host IP           |
| ---              | ---               |
|                  | 10.1.100.79 /18   |
|                  | 172.16.145.18 /20 |
|                  | 192.168.1.205 /30 | 

<br>

~~~
!@R1
show ip route static
conf t
 no ip route 10.1.1.5 255.255.255.255 10.1.1.2
 no ip route 10.1.1.6 255.255.255.255 10.1.1.2
 end
show ip route static
~~~

<br>

~~~
!@R1
conf t
 ip route 10.1.1.4 255.255.255.252 10.1.1.2
 end
show ip route static
~~~

<br>
<br>
<br>
<br>

__Configure a Network route on R3 destined for R1 & R2's connected network.__

<br>

~~~
!@R3
show ip route static
~~~

<br>

Check the Network Mask of an interface: 3 ways
~~~
!@R1
show run
show int e1/0
show ip route 
~~~

<br>

~~~
!@R3
show ip route static
conf t
 ip route 10.1.1.0 255.255.255.252 10.1.1.5
 end
show ip route static
~~~


<br>
<br>

---
&nbsp;


__Configure R1 to be able to reach R4__

~~~
!@R1
conf t
 ip route 10.1.1.8 255.255.255.252 10.1.1.2
 end 
~~~

<br>

Verify:
~~~
!@R1
ping 10.1.1.9

vs

ping 10.1.1.10
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 07: Configure a static network route on R4 destined to R1's e1/0 interface
~~~
!@R4
conf t
 ip route 10.1.1.__ 255.255.255.252 10.1.1.__
 end
~~~

<br>
<br>
<br>
<br>
<br>


<br>
<br>

---
&nbsp;

### Static Route via Exit Interface

Configure a static host route on R3, destined for R4's 10.1.4.9 IP using both a next-hop address and interface.

~~~
!@R3
conf t
 ip route 10.1.4.9 255.255.255.255 e1/2 10.1.1.10
 end
~~~


<br>
<br>

---
&nbsp;


## 🔀 Default Route & Floating Static Route
~~~
!@cmd
route print
~~~

__Administrative Distance__ - Trustworthiness & Reliability of a Route Source

| AD Value | Trust Value               |
| ---      | ---                       |
| 0        | Most Trusted              |
| 1 - 254  | Lower Value, Higher Trust |
| 255      | Untrusted, Discarded      |

<br>

~~~
!@A1
conf t
 ip route 0.0.0.0 0.0.0.0 192.168.1.129 1
 ip route 0.0.0.0 0.0.0.0 192.168.1.130 10
 end
~~~

<br>

The Primary link went down:
~~~
!@A1
show ip route static
conf t
 no ip route 0.0.0.0 0.0.0.0 192.168.1.129 1
 end
show ip route static
~~~

<br>

The Primary link has been fixed
~~~
!@A1
conf t
 ip route 0.0.0.0 0.0.0.0 192.168.1.129 1
 end
show ip route static
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 08: Configure default routes on A2 with the following settings:
- __C2__ must be the __primary gateway__
- __C1__ must be the __secondary gateway__
- The __AD__ must have a difference of __10__

~~~
!@A2
conf t
 ip route 0.0.0.0 0.0.0.0 192.168.1.__  __
 ip route 0.0.0.0 0.0.0.0 192.168.1.__  __
 end
~~~

<br>
<br>
<br>
<br>
<br>
<br>
<br>

---
&nbsp;


## Path Selection Process
1. &nbsp;
2. &nbsp;
3. &nbsp;

<br>

~~~
!@P1
conf t
 ip route 192.168.1.128 255.255.255.224 10.2.1.1
 end
ping 192.168.1.129
~~~

<br>

__Routing Policies__, configure routing with the __least hop count possible__.

<br>

Verify:

~~~
!@P1
traceroute 192.168.1.129
traceroute 192.168.1.130
traceroute 192.168.1.131
traceroute 192.168.1.132
~~~

<br>

Why does P1 need to take 2 hop counts to reach C2's VLAN 100?

<br>

Configure a host static route that takes advantage of the longest prefix rule to allow P1 to go directly to C2 instead of C1.
~~~
!@P1
conf t
 ip route 192.168.1.130 255.255.255.255 10.2.1.2
 end
~~~

<br>

Verify:
~~~
!@P1
show ip route static

traceroute 192.168.1.129
traceroute 192.168.1.131
traceroute 192.168.1.132

vs

traceroute 192.168.1.130
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 09: Configure static routes on P2, destined for VLAN 100 with the least hop counts possible to D1, D2, A1, and A2.

~~~
!@P2
conf t
 ip route 192.168.1.__  __.__.__.__  __.__.__.__
 ip route 192.168.1.__  __.__.__.__  __.__.__.__
 end
~~~

<br>
<br>
<br>
<br>
<br>

---
&nbsp;


### 🎯 Excercise 10: Configure static routes to allow P1 to ping Google (8.8.8.8)
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<br>
<br>

---
&nbsp;


## 🔀 Dynamic Routing
~~~
!@C1,C2,R4
show version
~~~

<br>

If all Cisco, use __EIGRP__


&nbsp;
---
&nbsp;


## 🔀 EIGRP
Steps in configuring EIGRP
1. Decide on an ASN
2. Determine Connected Networks
3. Advertise

~~~
!@R4
conf t
 router eigrp 100
  no auto-summary
  network 10.1.4.8 0.0.0.3
  network 10.1.4.4 0.0.0.3
  end
~~~

~~~
!@C1
config t
 router eigrp 100
  no auto-summary
  network 10.1.4.4 0.0.0.3
  network 10.2.1.0 0.0.0.255
  network 10.2.2.0 0.0.0.255
  network 192.168.1.128 0.0.0.31
end
~~~

<br>
<br>

---
&nbsp;

### 🎯 Excercise 11: Configure EIGRP on C2. Advertise all connected routes.
~~~
!@C2
config t
 router ____  ____
  no auto-summary
  network __.__.__.__  __.__.__.__
  network __.__.__.__  __.__.__.__
  network __.__.__.__  __.__.__.__
  network __.__.__.__  __.__.__.__
  end
~~~


<br>
<br>
<br>
<br>
<br>
<br>

---
&nbsp;


### OPTIONAL
### Named EIGRP / Multi Address-Family EIGRP
When you are using NEXUS, address family is required.

~~~
!@R4
conf t
 router eigrp CCNPLEVEL
  address-family ipv4 unicast autonomous-system 100
   network 10.1.4.8 0.0.0.3
   network 10.1.4.4 0.0.0.3
   end
~~~

~~~
!@D1
conf t
 router eigrp CCNPLEVEL
  address-family ipv4 unicast autonomous-system 100
   network 10.1.4.4 0.0.0.3
   network 10.2.1.0 0.0.0.255
   network 10.2.2.0 0.0.0.255
   network 192.168.1.128 0.0.0.31
   end
~~~

~~~
!@D2
conf t
 router eigrp CCNPLEVEL
  address-family ipv4 unicast autonomous-system 100
   network 10.1.4.8 0.0.0.3
   network 10.2.1.0 0.0.0.255
   network 10.2.2.0 0.0.0.255
   network 192.168.1.128 0.0.0.31
   end
~~~


&nbsp;
---
&nbsp;


~~~
!@R4
show ip route
~~~


<br>
<br>


### What makes __EIGRP__ a __Distance Vector Protocol__?
~~~
!@C1
conf t
 int e3/3
  no shut
 monitor session 1 source interface e1/2
 monitor session 1 destination interface e3/3
 end
~~~

<br>

~~~
!@R4
show ip protocols
show ip eigrp topology
~~~

<br>
<br>

### EIGRP Metric
*EIGRP Metric Formula*

<br>

__EIGRP Path Selection:__

| Device | RD  | FD  | Metric Path |
| ---    | --- | --- | ---         |
| C1     |     |     |             |
| C2     |     |     |             |

<br>

1. Reported Distance (__RD__)  
2. Feasible Distance (__FD__)  
3. Successor (Primary : Lowest Cost)  
4. Feasible Successor (Backup)  

<br>

~~~
!@R4
conf t
int e1/1
 delay 10000
 end
~~~

<br>

__Feasability Condition__ - An EIGRP route is a feasible successor route if the RD from the neighbor is less than the FD of the successor route.

<br>
<br>

| Device | FD  | AD/RD | Role |
| ---    | --- | ---   | ---  |
| A      | 46  | 37    |      |
| B      | 49  | 45    |      |
| C      | 44  | 29    |      |
| D      | 51  | 42    |      |
| E      | 62  | 58    |      |


&nbsp;
---
&nbsp;


### EIGRP Loadbalancing Unequal Cost Paths - Variance
~~~
!@R4
conf t
 router eigrp 100
  variance 2
  traffic-share balanced
  end
~~~


<br>
<br>

---
&nbsp;


## 🔀 OSPF
What Routing protocol to use if __Multi-Vendor__? __OSPF__

<br>
<br>

### Single Area OSPF
Advertise Connected Routes:
~~~
!@R3
show ip route | inc C
~~~

~~~
!@R3
conf t
 router ospf 1
  router-id 3.3.3.3
  network 3.3.3.3 0.0.0.0 area 0
  network 10.1.1.8 0.0.0.3 area 0
  network 10.1.1.4 0.0.0.3 area 0
  end
~~~

<br>

~~~
!@R4
conf t
 router ospf 1
  router-id 4.4.4.4
  network 4.4.4.4 0.0.0.3 area 0
  network 10.1.1.8 0.0.0.3 area 0
  end
~~~


<br>
<br>

---
&nbsp;


### 🎯 Excercise 13: Configure OSPF on R2 with the following settings:
- Process ID must be 1
- Advertise all connected routes to the correct OSPF Area
- R2's Router ID belongs to the Backbone Area
- Set R2's router id for OSPF as its loopback 2 IP

~~~
!@R2
conf t





  end
~~~

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


<br>
<br>

---
&nbsp;


### OSPF Interface-specific network advertisement.
~~~
!@R1
conf t
 router ospf 1
  router-id 1.1.1.1
  exit
 int lo1
  ip ospf 1 area 0
  exit
 int e1/0
  ip ospf 1 area 0
  end
~~~


&nbsp;
---
&nbsp;


### What makes a dynamic routing protocol dynamic?

~~~
!@R4
conf t
 int lo4
  shut
  end
~~~

~~~
!@R1
show ip route ospf
show ip ospf route
~~~

<br>

Bring back Loopback 4.4.4.4

<br>

~~~
!@R4
conf t
 int lo4
  no shut
  end
~~~


<br>
<br>

---
&nbsp;


### OSPF Network Types and Priorities.
### 🎯 Excercise 14: Ensure R3 is the DR for all its connected networks by completing the following tasks:
- Eliminate the need for a DR/BDR election between R4 & R3
- Configure R1 to be ineligible to become a DR/BDR
- Configure R2 with the highest priority on its e1/2 interface.

~~~
!@R4
conf t
 int e1/2
  ip ospf network point-to-point
  end
~~~

<br>

~~~
!@R3
conf t
 int e1/2
  ip ospf network point-to-point
  end
~~~

<br>

~~~
!@R2
conf t
 int e1/2
  ip ospf priority 255
  end
~~~

<br>

~~~
!@R1
conf t
 int e1/0
  ip ospf priority 0
  end
~~~

<br>

Verify:
~~~
!@R4,R3,R2,R1
show ip ospf neighbor
~~~


<br>
<br>

---
&nbsp;


### Capture Hello Packets
~~~
!@R4
conf t
 int e3/3
  no shut
  ip add 208.8.8.100 255.255.255.0
  ip ospf 1 area 34
  end
~~~

<br>

~~~
!@CoreBABA
conf t
 monitor session 1 source int g0/1
 monitor session 1 destination int fa0/1,fa0/9
 end
~~~

<br>

__WireShark__ - Capture Packets from __VMNet8__ & filter __OSPF__  

<br>
<br>


<br>
<br>

---
&nbsp;


### Neighborship vs Adjacency

1. __Mismatched Network Type__

~~~
!@R3
conf t
 int e1/2
  no ip ospf network point-to-point
  end
show ip ospf neighbor
clear ip ospf process
yes
~~~

<br>

~~~
!@R4
show ip route ospf
~~~

<br>

~~~
!@R3 & R4
show ip ospf int e1/2
~~~

<br>

Determine the issue why R3 & R4 fail to form an adjacency:

<br>
<br>

Fix the adjacency:

~~~
!@R3
conf t
 int e1/2
  ip ospf network point-to-point
  end
show ip ospf neighbor
clear ip ospf process
yes
~~~

&nbsp;
---
&nbsp;

2. __Mismatched Hello & Dead Timers__
~~~
!@R2
conf t
 int e1/2
  ip ospf hello-interval 20
  ip ospf dead-interval 60
  end
show ip ospf neighbor
clear ip ospf process
yes
~~~

~~~
!@R2
show ip ospf int e1/2
~~~

~~~
!@R1
show ip ospf int e1/0
~~~

<br>

Determine the issue why R2 & R1 fail to form an adjacency:

<br>
<br>

Fix the adjacency:
~~~
!@R2
conf t
 int e1/2
  ip ospf hello-interval 10
  ip ospf dead-interval 40
  end
show ip ospf neighbor
clear ip ospf process
~~~


<br>
<br>

---
&nbsp;


### OSPF Passive-Interface
Configure loopback interfaces to not send hello packets

~~~
!@R1
conf t
 router ospf 1
  passive-interface lo1
  end
~~~

<br>

~~~
!@R2
conf t
 router ospf 1
  passive-interface lo2
  end
~~~

<br>

~~~
!@R3
conf t
 router ospf 1
  passive-interface lo3
  end
~~~

<br>

~~~
!@R4
conf t
 router ospf 1
  passive-interface lo4
  end
~~~


<br>
<br>

---
&nbsp;


### OSPF & EIGRP Redistribution
~~~
!@R4
config T
 router eigrp 100
  redistribute ospf 1
  exit
 router ospf 1
  redistribute eigrp 100 subnets
end
~~~

<br>

or

<br>

~~~
!@R4
conf t
 router eigrp CCNPLEVEL
  address-family ipv4 unicast autonomous-system 100
   topology base
    redistribute ospf 1
	exit
   exit
  exit
 router ospf 1
  redistribute eigrp 100 subnets
    end
~~~


<br>
<br>

---
&nbsp;


## Path Selection Process 
1. 
2. 
3. 

<br>

| Legend | Routing Protocol | Administrative Distance | Metric |
| ---    | ---              | ---                     | ---    |
| C      | Connected        |                         |        |
| S      | Static           |                         |        |
| D      | EIGRP            |                         |        |
| D EX   | External EIGRP   |                         |        |
| O      | OSPF             |                         |        |
| O E2   | External T5 OSPF |                         |        |

~~~
!@R4, D1, R3
show ip route
~~~

<br>
<br>

### OSPF Metric Cost 
Interface Cost = Reference Bandwidth / Interface Bandwidth
~~~
!@R3
show ip ospf | inc band
~~~

~~~
!@R1,R2,R3,R4
conf t
 router ospf 1
  auto-cost reference-bandwidth 100000
  end
~~~


<br>
<br>

---
&nbsp;


### Link-State Routing Protocol
~~~
!@C1
conf t
 router ospf 1
  network 10.1.4.4 0.0.0.3 area 34
  auto-cost reference-bandwidth 100000
 !
 no monitor session 1
 monitor session 1 source int e1/1
 monitor session 1 destination int e3/3
end
~~~

<br>

~~~
!@R4
conf t
 router ospf 1
  network 10.1.4.4 0.0.0.3 area 34
  auto-cost reference-bandwidth 100000
 !
 int e3/3
  shut
  end
~~~


__LSU__ - Link-State Updates  
__LSA__ - Link-State Advertisement  

<br>

- Type 1 LSA - (__O__) Router LSA : Router info

~~~
!@R4
conf t
 router ospf 1
  no network 10.1.4.4 0.0.0.3 area 34
  network 10.1.4.4 0.0.0.3 area 34
  end
~~~

- Type 2 LSA - (__O__) Network LSA : via DR/BDR Network Routes

~~~
!@R4
conf t
 router ospf 1
  no network 4.4.4.4 0.0.0.3 area 34
  network 4.4.4.4 0.0.0.3 area 34
  end
~~~

- Type 3 LSA - (__O IA__) Summary LSA
- Type 5 LSA - (__O E2__) AS-External LSA

<br>

~~~
!@EDGE
conf t
 int lo#$34T#
  ip add #$34T#.#$34T#.#$34T#.#$34T# 255.255.255.255
  ip ospf 1 area #$34T#
  end
clear ip ospf process
yes
~~~

~~~
!@R3
show ip ospf database
show ip ospf database network
~~~


&nbsp;
---
&nbsp;


### OSPF States
D: __Down__ - The initial state where no hello packets have been received from a neighbor  

<br>

I: __Init__ - A hello packet has been received from a neighbor, but that neighbor's Router ID was not included in the hello packet, indicating a lack of bidirectional communication  

<br>

T: __Two-way__ - Bidirectional communication is established, as both routers have received each other's Router IDs in hello packets. DR/BDR Election occurs.  

<br>

E: __Exstart__ - Routers determine who will be the master and who will be the slave for the upcoming database exchange. The router with the higher Router ID becomes the master and begins the exchange of Database Description (DBD) packets, synchronizing sequence numbers.  

<br>

E: __Exchange__ - Routers exchange DBD packets to describe their Link State Databases (LSDBs). They compare the contents and identify any missing link-state information  

<br>

L: __Loading__ - Routers request the missing link-state information by sending Link-State Requests (LSRs). They then receive Link-State Updates (LSUs) and acknowledge them with Link-State Acknowledgements (LSAs)  

<br>

F: __Full__ - the LSDBs are fully synchronized and identical between the adjacent routers. The routers have all the necessary information to form a complete network map and are ready to share routing data  

<br>

Attempt to view OSPF States

~~~
!@R2 & R1
clear ip ospf process
yes
show ip ospf neighbor
~~~


<br>
<br>

---
&nbsp;


### Route Summarization

Summarize Routes:
1. OCTET
1. RANGE 
2. iTANCHA


<br>
<br>

---
&nbsp;


### 🎯 Exercise: Summarize the ff:
- 10.1.1.0/30
- 10.1.1.4/30
- 10.1.1.8/30


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

---
&nbsp;


### 🎯 Exercise: Summarize the ff:
- 10.1.20.8/29
- 10.1.20.16/28
- 10.1.20.32/30
- 10.1.20.64/26



<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

---
&nbsp;


### 🎯 Exercise: Summarize the ff:
- 10.144.0.0/13
- 10.157.0.0/16
- 10.171.128.0/17
- 10.183.64.0/18
- 10.190.240.0/20



<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

---
&nbsp;


~~~
!@R2
conf t
 int lo8
  ip add 10.10.8.1 255.255.255.0
  ip ospf 1 area 12
 int lo9
  ip add 10.10.9.1 255.255.255.0
  ip ospf 1 area 12
 int lo10
  ip add 10.10.10.1 255.255.255.0
  ip ospf 1 area 12
 int lo11
  ip add 10.10.11.1 255.255.255.0
  ip ospf 1 area 12
 int lo33
  ip add 10.10.33.1 255.255.255.128
  ip ospf 1 area 12
 int lo34
  ip add 10.10.33.129 255.255.255.128
  ip ospf 1 area 12
 int lo35
  ip add 10.10.34.1 255.255.255.128
  ip ospf 1 area 12
 int lo36
  ip add 10.10.34.129 255.255.255.128
  ip ospf 1 area 12
  exit
 int range lo8-11,lo33-36
  ip ospf network point-to-point
 router ospf 1
  passive-interface lo8
  passive-interface lo9
  passive-interface lo10
  passive-interface lo11
  passive-interface lo33
  passive-interface lo34
  passive-interface lo35
  passive-interface lo36
  end
~~~


<br>
<br>


### 🎯 Exercise: Summarize the ff:
- 10.10.8.0 /24
- 10.10.9.0 /24
- 10.10.10.0 /24
- 10.10.11.0 /24


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

---
&nbsp;


### 🎯 Excercise: Summarize routes from loopback 33 - loopback 36
- 10.10.33.0   /25
- 10.10.33.128 /25
- 10.10.34.0   /25
- 10.10.34.128 /25



<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

---
&nbsp;


Remove All summarizations
~~~
!@R2
conf t
 router ospf 1
  no area 12 range 10.10.8.0 255.255.252.0
  no area 12 range 10.10.32.0 255.255.252.0
  end
~~~


<br>
<br>

---
&nbsp;


### BGP
R1 = ASN 1  
I1 & I4(GOOGLE DNS) = ASN 45  
I2 = ASN 2  
I3 = ASN 1  

<br>
<br>

~~~
!@R1
conf t
 router bgp 1
  bgp log-neighbor-changes
   neighbor 208.8.8.4 remote-as 45
   neighbor 207.7.7.2 remote-as 2
   neighbor 209.9.9.3 remote-as 3
   address-family ipv4
	neighbor 208.8.8.4 activate
    neighbor 207.7.7.2 activate
    neighbor 209.9.9.3 activate
    network 207.7.7.0 mask 255.255.255.0
    network 208.8.8.0 mask 255.255.255.0
    network 209.9.9.0 mask 255.255.255.0
    end
~~~

<br>

~~~
!@I1 - CONVERGE
conf t
 router bgp 45
  bgp log-neighbor-changes
  neighbor 24.2.4.2 remote-as 2
  neighbor 45.4.5.5 remote-as 45
  neighbor 208.8.8.1 remote-as 1
  address-family ipv4
   neighbor 24.2.4.2 activate
   neighbor 45.4.5.5 activate
   neighbor 208.8.8.1 activate
   network 208.8.8.0 mask 255.255.255.0
   network 24.2.4.0 mask 255.255.255.0
   network 44.44.44.44 mask 255.255.255.255
   network 45.4.5.0 mask 255.255.255.0
   end
~~~

<br>

~~~
!@I3 - GLOBE
conf t
 router bgp 3
  bgp log-neighbor-changes
  neighbor 32.3.2.2 remote-as 2
  neighbor 35.3.5.5 remote-as 45
  neighbor 209.9.9.1 remote-as 1
  address-family ipv4
   neighbor 32.3.2.2 activate
   neighbor 35.3.5.5 activate
   neighbor 209.9.9.1 activate
   network 209.9.9.0 mask 255.255.255.0
   network 32.3.2.0 mask 255.255.255.0
   network 33.33.33.33 mask 255.255.255.255
   network 35.3.5.0 mask 255.255.255.0
   end
~~~

<br>

~~~
!@I4 - GOOGLE
config t
 router bgp 45
  bgp log-neighbor-changes
  neighbor 25.2.5.2 remote-as 2
  neighbor 35.3.5.3 remote-as 3
  neighbor 45.4.5.4 remote-as 45
  address-family ipv4
   neighbor 25.2.5.2 activate
   neighbor 35.3.5.3 activate
   neighbor 45.4.5.4 activate
   network 8.8.8.8 mask 255.255.255.255
   network 55.55.55.55 mask 255.255.255.255
   network 25.2.5.0 mask 255.255.255.0
   network 35.3.5.0 mask 255.255.255.0
   network 45.4.5.0 mask 255.255.255.0
   end
~~~


<br>
<br>

---
&nbsp;


### 🎯 Excercise: Configure BGP on I2(PLDT). Set the ASN number to 2.
- Advertise the loopback IP

~~~
!@I2 - PLDT
config t
 router bgp __
 bgp log-neighbor-changes
 neighbor __.__.__.__ remote-as __
 neighbor __.__.__.__  remote-as __
 neighbor __.__.__.__  remote-as __
 neighbor __.__.__.__  remote-as __
 address-family __
  neighbor __.__.__.__  ____
  neighbor __.__.__.__  ____
  neighbor __.__.__.__  ____
  neighbor __.__.__.__  ____
  network __.__.__.__ mask __.__.__.__
  network __.__.__.__ mask __.__.__.__
  network __.__.__.__ mask __.__.__.__
  network __.__.__.__ mask __.__.__.__
  network __.__.__.__ mask __.__.__.__
  end
~~~

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


<br>
<br>

---
&nbsp;


### ANSWER

<details>
<summary>Show Answer</summary>

~~~
!@I2 - PLDT
config t
 router bgp 2
 bgp log-neighbor-changes
 neighbor 24.2.4.4 remote-as 45
 neighbor 25.2.5.5 remote-as 45
 neighbor 32.3.2.3 remote-as 3
 neighbor 207.7.7.1 remote-as 1
 address-family ipv4
  neighbor 24.2.4.4 activate
  neighbor 25.2.5.5 activate
  neighbor 32.3.2.3 activate
  neighbor 207.7.7.1 activate
  network 207.7.7.0 mask 255.255.255.0
  network 22.22.22.22 mask 255.255.255.255
  network 24.2.4.0 mask 255.255.255.0
  network 25.2.5.0 mask 255.255.255.0
  network 32.3.2.0 mask 255.255.255.0
  end
~~~

</details>

<br>
<br>

Verify:

~~~
!@I2 - PLDT
show bgp summary
~~~


<br>
<br>

---
&nbsp;


### BGP - OSPF Default Route Injection
~~~
!@R1
conf t
 ip route 0.0.0.0 0.0.0.0 208.8.8.4 10
 ip route 0.0.0.0 0.0.0.0 209.9.9.3 20
 ip route 0.0.0.0 0.0.0.0 207.7.7.2 30
 router ospf 1
  default-information originate
  end
~~~

<br>

~~~
!@R1
show ip route
~~~

&nbsp;
---
&nbsp;

## Path Selection Process : Admin Distance & Metric Cost
1. __Longest Prefix Match (LPM)__  
2. __Administrative Distance__
3. __Metric Cost__

<br>

| Legend | Routing Protocol | Administrative Distance | Metric |
| ---    | ---              | ---                     | ---    |
| C      | Connected        |                         |        |
| S      | Static           |                         |        |
| D      | EIGRP            |                         |        |
| D EX   | External EIGRP   |                         |        |
| O      | OSPF             |                         |        |
| O E2   | External T5 OSPF |                         |        |
| B      | Internal BGP     |                         |        |
| B      | External BGP     |                         |        |

<br>

~~~
!@R1, I1 - CONVERGE
show ip route
~~~


<br>
<br>

---
&nbsp;


### NAT
Step 1: Define INSIDE and OUTSIDE

~~~
!@R1
conf t
 int range e1/1-3
  ip nat outside
  exit
 int e1/0
  ip nat inside
  end
~~~

<br>
<br>

Step 2: Configure desired NAT

### Static NAT or 1:1
~~~
!@R1
conf t
 ip nat inside source static 10.1.1.2 208.8.8.10 
 ip nat inside source static 10.1.1.6 208.8.8.20
 ip nat inside source static 10.1.1.10 208.8.8.30
 end
show ip nat translations
~~~

<br>

10.1.1.2 = R2
10.1.1.6 = R3
10.1.1.10 = R4

~~~
!@R2, R3, R4
ping 8.8.8.8
~~~

<br>

~~~
INSIDE GLOBAL     INSIDE LOCAL         OUTSIDE LOCAL      OUTSIDE GLOBAL

~~~

<br>
<br>

&nbsp;
---
&nbsp;

### 🎯 Exercise 19: Configure Static NAT for the following devices:

(D1) 10.1.4.6 = 208.8.8.x
(D2) 10.1.4.10 = 207.7.7.x

~~~
!@R1
conf t
 ip nat inside source static __.__.__.__  __.__.__.__
 ip nat inside source static __.__.__.__  __.__.__.__
 end 
~~~


<br>

Verify with a ping to 8.8.8.8 on the devices, 
then use the show command to reveal translated IPs on R1.

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

&nbsp;
---
&nbsp;

### Dynamic NAT
Create an ACL to match traffic
~~~
!@R1
conf t
 access-list 1 permit 10.0.0.0 0.255.255.255
 access-list 1 permit 172.16.0.0 0.15.255.255
 access-list 1 permit 192.168.0.0 0.0.255.255
 !
 ip nat pool NATPOOL 209.9.9.10 209.9.9.20 netmask 255.255.255.0
 ip nat inside source list 1 pool NATPOOL
 end
~~~

<br>

Verify:
~~~
!@A1, A2
ping 8.8.8.8
~~~


<br>
<br>

---
&nbsp;


### PAT 1:Many
Add an OVERLOAD Keyword
~~~
!@R1
clear ip nat trans *
conf t
 ip nat inside source list 1 pool NATPOOL overload
 end
~~~

<br>

or 

<br>

~~~
!@R1
conf t
 ip nat inside source list 1 int e1/2 overload
 end
~~~


<br>
<br>

---
&nbsp;


### 🎯 Exercise 20: Configure P1, P2, S1, & S2 to successfully ping 8.8.8.8 using a static NAT assignment.

P1 = 207.7.7.201
P2 = 207.7.7.202
S1 = 209.9.9.201
S2 = 209.9.9.202

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

---
&nbsp;


## IPv6

<br>

### IPv6 compression rules  

1. 000a:000c:0000:0000:0000:0000:0000:0000/64
     =

<br>

3. 0000:0000:0000:0000:0000:0000:0000:0000/0
     = 

<br>

5. fe80:0000:0000:0000:000a:0000:0000:000f/64
     =

<br>

7. 2002:6500:0000:3000:0000:0000:0000:0000/64
     = 

<br>

9. 0000:0000:0000:0000:0000:0000:0000:0001/128
     = 

<br>

11. ff00:0000:0000:beef:a00a:0aa0:0000:0000/8
     = 


<br>
<br>

---
&nbsp;

### IPv6 subnetting

` 8i  4i  2i   1i    8i  4i  2i   1i     8i  4i  2i   1i    8i  4i  2i   1i `

<br>
<br>

__Determine where the slash is located__

/64 = (Hextet, Hexadecimal, i)  
/65 = (Hextet, Hexadecimal, i)  
/72 = (Hextet, Hexadecimal, i)  

<br>

/120 = (Hextet, Hexadecimal, i)  
/27  = (Hextet, Hexadecimal, i)  


<br>
<br>

---
&nbsp;


## IPV6 SUBNETTING (HOSTS):

### 1. Design an IPv6 network for 48 users using the available IPv6 address space of fec0:aabb:fafa:dada::/64

~~~
C:  
S: 
I: 

Compressed Version: 
~~~

|                      |                             |
| ---                  | ---                         |
| Network/Anycast:     |                             |
| First Valid:         |                             |
| Last Valid:          |                             |
|                      |                             |
| Not Network:         |                             |

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<br>
<br>

---
&nbsp;


### 2. Design an IPv6 network for 780 users using the available IPv6 address space of 2001:db8:b:efe:1::/64

~~~
C:  
S: 
I: 

Compressed Version: 
~~~

|                      |                             |
| ---                  | ---                         |
| Network/Anycast:     |                             |
| First Valid:         |                             |
| Last Valid:          |                             |
|                      |                             |
| Not Network:         |                             |

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<br>
<br>

---
&nbsp;

## IPV6 SUBNETTING (SUBNETS):

### 1. Subnet for 16 sites using 2001:db8:1:20::/64  Determine the First Subnet  

~~~
C:
A:
I:



Compressed Version: 
~~~

<br>

|                      |                                      |
| ---                  | ---                                  |
| Network/Anycast:     |                                      |
| First Valid:         |                                      |
| Last Valid:          |                                      |
|                      |                                      |
| Not Network:         |                                      |

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<br>
<br>

---
&nbsp;


### 2. Subnet for 78 sites using 2001:db8:2:5::/98  Determine the Third Subnet

~~~
C:
A:
I:



Compressed Version: 
~~~

<br>

|                      |                                      |
| ---                  | ---                                  |
| Network/Anycast:     |                                      |
| First Valid:         |                                      |
| Last Valid:          |                                      |
|                      |                                      |
| Not Network:         |                                      |

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<br>
<br>

---
&nbsp;

## IPV6 AUTOCONFIG vs IPV6 DHCP vs IPV6 EUI-64




















