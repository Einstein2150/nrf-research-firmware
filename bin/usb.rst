                                      1 ;--------------------------------------------------------
                                      2 ; File Created by SDCC : free open source ANSI-C Compiler
                                      3 ; Version 4.0.0 #11528 (Mac OS X x86_64)
                                      4 ;--------------------------------------------------------
                                      5 	.module usb
                                      6 	.optsdcc -mmcs51 --model-large
                                      7 	
                                      8 ;--------------------------------------------------------
                                      9 ; Public variables in this module
                                     10 ;--------------------------------------------------------
                                     11 	.globl _write_descriptor
                                     12 	.globl _write_device_string
                                     13 	.globl _handle_radio_request
                                     14 	.globl ___memcpy
                                     15 	.globl _strlen
                                     16 	.globl _memset
                                     17 	.globl _RFRDY
                                     18 	.globl _rfcsn
                                     19 	.globl _rfce
                                     20 	.globl _ien1
                                     21 	.globl _ien0
                                     22 	.globl _REGXC
                                     23 	.globl _REGXL
                                     24 	.globl _REGXH
                                     25 	.globl _TICKDV
                                     26 	.globl _RFDAT
                                     27 	.globl _P0DIR
                                     28 	.globl _P0
                                     29 	.globl _AESIA1
                                     30 	.globl _AESIV
                                     31 	.globl _usbcon
                                     32 	.globl _rfcon
                                     33 	.globl _rfctl
                                     34 	.globl _request
                                     35 	.globl _setupbuf
                                     36 	.globl _out1buf
                                     37 	.globl _in1buf
                                     38 	.globl _in0buf
                                     39 	.globl _init_usb
                                     40 	.globl _usb_reset_config
                                     41 	.globl _usb_irq
                                     42 	.globl _handle_setup_request
                                     43 ;--------------------------------------------------------
                                     44 ; special function registers
                                     45 ;--------------------------------------------------------
                                     46 	.area RSEG    (ABS,DATA)
      000000                         47 	.org 0x0000
                           0000E6    48 _rfctl	=	0x00e6
                           000090    49 _rfcon	=	0x0090
                           0000A0    50 _usbcon	=	0x00a0
                           0000F2    51 _AESIV	=	0x00f2
                           0000F5    52 _AESIA1	=	0x00f5
                           000080    53 _P0	=	0x0080
                           000094    54 _P0DIR	=	0x0094
                           0000E5    55 _RFDAT	=	0x00e5
                           0000AB    56 _TICKDV	=	0x00ab
                           0000AB    57 _REGXH	=	0x00ab
                           0000AC    58 _REGXL	=	0x00ac
                           0000AD    59 _REGXC	=	0x00ad
                           0000A8    60 _ien0	=	0x00a8
                           0000B8    61 _ien1	=	0x00b8
                                     62 ;--------------------------------------------------------
                                     63 ; special function bits
                                     64 ;--------------------------------------------------------
                                     65 	.area RSEG    (ABS,DATA)
      000000                         66 	.org 0x0000
                           000090    67 _rfce	=	0x0090
                           000091    68 _rfcsn	=	0x0091
                           0000C0    69 _RFRDY	=	0x00c0
                                     70 ;--------------------------------------------------------
                                     71 ; overlayable register banks
                                     72 ;--------------------------------------------------------
                                     73 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                         74 	.ds 8
                                     75 	.area REG_BANK_1	(REL,OVR,DATA)
      000008                         76 	.ds 8
                                     77 ;--------------------------------------------------------
                                     78 ; overlayable bit register bank
                                     79 ;--------------------------------------------------------
                                     80 	.area BIT_BANK	(REL,OVR,DATA)
      000020                         81 bits:
      000020                         82 	.ds 1
                           008000    83 	b0 = bits[0]
                           008100    84 	b1 = bits[1]
                           008200    85 	b2 = bits[2]
                           008300    86 	b3 = bits[3]
                           008400    87 	b4 = bits[4]
                           008500    88 	b5 = bits[5]
                           008600    89 	b6 = bits[6]
                           008700    90 	b7 = bits[7]
                                     91 ;--------------------------------------------------------
                                     92 ; internal ram data
                                     93 ;--------------------------------------------------------
                                     94 	.area DSEG    (DATA)
      000010                         95 _write_device_string_sloc0_1_0:
      000010                         96 	.ds 2
                                     97 ;--------------------------------------------------------
                                     98 ; overlayable items in internal ram 
                                     99 ;--------------------------------------------------------
                                    100 ;--------------------------------------------------------
                                    101 ; indirectly addressable internal ram data
                                    102 ;--------------------------------------------------------
                                    103 	.area ISEG    (DATA)
                                    104 ;--------------------------------------------------------
                                    105 ; absolute internal ram data
                                    106 ;--------------------------------------------------------
                                    107 	.area IABS    (ABS,DATA)
                                    108 	.area IABS    (ABS,DATA)
                                    109 ;--------------------------------------------------------
                                    110 ; bit data
                                    111 ;--------------------------------------------------------
                                    112 	.area BSEG    (BIT)
                                    113 ;--------------------------------------------------------
                                    114 ; paged external ram data
                                    115 ;--------------------------------------------------------
                                    116 	.area PSEG    (PAG,XDATA)
                                    117 ;--------------------------------------------------------
                                    118 ; external ram data
                                    119 ;--------------------------------------------------------
                                    120 	.area XSEG    (XDATA)
                           00C700   121 _in0buf	=	0xc700
                           00C680   122 _in1buf	=	0xc680
                           00C640   123 _out1buf	=	0xc640
                           00C7E8   124 _setupbuf	=	0xc7e8
      00800A                        125 _configured:
      00800A                        126 	.ds 1
      00800B                        127 _write_device_string_string_65536_81:
      00800B                        128 	.ds 3
      00800E                        129 _write_descriptor_desc_len_65536_84:
      00800E                        130 	.ds 1
      00800F                        131 _handle_setup_request_handled_65536_86:
      00800F                        132 	.ds 1
                                    133 ;--------------------------------------------------------
                                    134 ; absolute external ram data
                                    135 ;--------------------------------------------------------
                                    136 	.area XABS    (ABS,XDATA)
                                    137 ;--------------------------------------------------------
                                    138 ; external initialized ram data
                                    139 ;--------------------------------------------------------
                                    140 	.area XISEG   (XDATA)
      0080B3                        141 _nordic_bootloader:
      0080B3                        142 	.ds 2
      0080B5                        143 _logitech_bootloader:
      0080B5                        144 	.ds 2
      0080B7                        145 _request::
      0080B7                        146 	.ds 2
                                    147 	.area HOME    (CODE)
                                    148 	.area GSINIT0 (CODE)
                                    149 	.area GSINIT1 (CODE)
                                    150 	.area GSINIT2 (CODE)
                                    151 	.area GSINIT3 (CODE)
                                    152 	.area GSINIT4 (CODE)
                                    153 	.area GSINIT5 (CODE)
                                    154 	.area GSINIT  (CODE)
                                    155 	.area GSFINAL (CODE)
                                    156 	.area CSEG    (CODE)
                                    157 ;--------------------------------------------------------
                                    158 ; global & static initialisations
                                    159 ;--------------------------------------------------------
                                    160 	.area HOME    (CODE)
                                    161 	.area GSINIT  (CODE)
                                    162 	.area GSFINAL (CODE)
                                    163 	.area GSINIT  (CODE)
                                    164 ;--------------------------------------------------------
                                    165 ; Home
                                    166 ;--------------------------------------------------------
                                    167 	.area HOME    (CODE)
                                    168 	.area HOME    (CODE)
                                    169 ;--------------------------------------------------------
                                    170 ; code
                                    171 ;--------------------------------------------------------
                                    172 	.area CSEG    (CODE)
                                    173 ;------------------------------------------------------------
                                    174 ;Allocation info for local variables in function 'init_usb'
                                    175 ;------------------------------------------------------------
                                    176 ;ms_elapsed                Allocated with name '_init_usb_ms_elapsed_65536_74'
                                    177 ;__1310720005              Allocated with name '_init_usb___1310720005_131072_75'
                                    178 ;us                        Allocated with name '_init_usb_us_196608_76'
                                    179 ;------------------------------------------------------------
                                    180 ;	src/usb.c:29: bool init_usb() 
                                    181 ;	-----------------------------------------
                                    182 ;	 function init_usb
                                    183 ;	-----------------------------------------
      000118                        184 _init_usb:
                           000007   185 	ar7 = 0x07
                           000006   186 	ar6 = 0x06
                           000005   187 	ar5 = 0x05
                           000004   188 	ar4 = 0x04
                           000003   189 	ar3 = 0x03
                           000002   190 	ar2 = 0x02
                           000001   191 	ar1 = 0x01
                           000000   192 	ar0 = 0x00
                                    193 ;	src/usb.c:32: configured = false;
      000118 90 80 0A         [24]  194 	mov	dptr,#_configured
      00011B E4               [12]  195 	clr	a
      00011C F0               [24]  196 	movx	@dptr,a
                                    197 ;	src/usb.c:35: usbcon = 0x40; 
      00011D 75 A0 40         [24]  198 	mov	_usbcon,#0x40
                                    199 ;	src/usb.c:38: usbcs |= 0x08;
      000120 90 C7 D6         [24]  200 	mov	dptr,#0xc7d6
      000123 E0               [24]  201 	movx	a,@dptr
      000124 44 08            [12]  202 	orl	a,#0x08
      000126 F0               [24]  203 	movx	@dptr,a
                                    204 ;	src/nRF24LU1P.h:35: inline void delay_us(uint16_t us) { do nop_us(); while(--us); }
      000127 7E 50            [12]  205 	mov	r6,#0x50
      000129 7F C3            [12]  206 	mov	r7,#0xc3
      00012B                        207 00104$:
      00012B 00               [12]  208 	nop 
      00012C 00               [12]  209 	nop 
      00012D 00               [12]  210 	nop 
      00012E 00               [12]  211 	nop 
      00012F 1E               [12]  212 	dec	r6
      000130 BE FF 01         [24]  213 	cjne	r6,#0xff,00127$
      000133 1F               [12]  214 	dec	r7
      000134                        215 00127$:
      000134 EE               [12]  216 	mov	a,r6
      000135 4F               [12]  217 	orl	a,r7
      000136 70 F3            [24]  218 	jnz	00104$
                                    219 ;	src/usb.c:40: usbcs &= ~0x08;
      000138 90 C7 D6         [24]  220 	mov	dptr,#0xc7d6
      00013B E0               [24]  221 	movx	a,@dptr
      00013C 54 F7            [12]  222 	anl	a,#0xf7
      00013E F0               [24]  223 	movx	@dptr,a
                                    224 ;	src/usb.c:43: usb_reset_config();
      00013F 12 01 4C         [24]  225 	lcall	_usb_reset_config
                                    226 ;	src/usb.c:46: while(!configured);
      000142                        227 00101$:
      000142 90 80 0A         [24]  228 	mov	dptr,#_configured
      000145 E0               [24]  229 	movx	a,@dptr
      000146 60 FA            [24]  230 	jz	00101$
                                    231 ;	src/usb.c:49: return true;
      000148 75 82 01         [24]  232 	mov	dpl,#0x01
                                    233 ;	src/usb.c:50: }
      00014B 22               [24]  234 	ret
                                    235 ;------------------------------------------------------------
                                    236 ;Allocation info for local variables in function 'usb_reset_config'
                                    237 ;------------------------------------------------------------
                                    238 ;	src/usb.c:53: void usb_reset_config()
                                    239 ;	-----------------------------------------
                                    240 ;	 function usb_reset_config
                                    241 ;	-----------------------------------------
      00014C                        242 _usb_reset_config:
                                    243 ;	src/usb.c:56: usbien = 0x11;  // USB reset and setup data valid
      00014C 90 C7 AE         [24]  244 	mov	dptr,#0xc7ae
      00014F 74 11            [12]  245 	mov	a,#0x11
      000151 F0               [24]  246 	movx	@dptr,a
                                    247 ;	src/usb.c:57: in_ien = 0x00;  // Disable EP IN interrupts
      000152 90 C7 AC         [24]  248 	mov	dptr,#0xc7ac
      000155 E4               [12]  249 	clr	a
      000156 F0               [24]  250 	movx	@dptr,a
                                    251 ;	src/usb.c:58: out_ien = 0x02; // Enable EP1 OUT interrupt
      000157 90 C7 AD         [24]  252 	mov	dptr,#0xc7ad
      00015A 74 02            [12]  253 	mov	a,#0x02
      00015C F0               [24]  254 	movx	@dptr,a
                                    255 ;	src/usb.c:59: ien1 = 0x10;    // Enable USB interrupt
      00015D 75 B8 10         [24]  256 	mov	_ien1,#0x10
                                    257 ;	src/usb.c:60: in_irq = 0x1F;  // Clear IN IRQ flags
      000160 90 C7 A9         [24]  258 	mov	dptr,#0xc7a9
      000163 74 1F            [12]  259 	mov	a,#0x1f
      000165 F0               [24]  260 	movx	@dptr,a
                                    261 ;	src/usb.c:61: out_irq = 0x1F; // Clear OUT IRQ flags
      000166 90 C7 AA         [24]  262 	mov	dptr,#0xc7aa
      000169 F0               [24]  263 	movx	@dptr,a
                                    264 ;	src/usb.c:64: inbulkval = 0x02;
      00016A 90 C7 DE         [24]  265 	mov	dptr,#0xc7de
      00016D 74 02            [12]  266 	mov	a,#0x02
      00016F F0               [24]  267 	movx	@dptr,a
                                    268 ;	src/usb.c:65: outbulkval = 0x02;
      000170 90 C7 DF         [24]  269 	mov	dptr,#0xc7df
      000173 F0               [24]  270 	movx	@dptr,a
                                    271 ;	src/usb.c:66: inisoval = 0x00;
      000174 90 C7 E0         [24]  272 	mov	dptr,#0xc7e0
      000177 E4               [12]  273 	clr	a
      000178 F0               [24]  274 	movx	@dptr,a
                                    275 ;	src/usb.c:67: outisoval = 0x00;  
      000179 90 C7 E1         [24]  276 	mov	dptr,#0xc7e1
      00017C F0               [24]  277 	movx	@dptr,a
                                    278 ;	src/usb.c:70: bout1addr = 32;
      00017D 90 C7 81         [24]  279 	mov	dptr,#0xc781
      000180 74 20            [12]  280 	mov	a,#0x20
      000182 F0               [24]  281 	movx	@dptr,a
                                    282 ;	src/usb.c:71: bout2addr = 64;
      000183 90 C7 82         [24]  283 	mov	dptr,#0xc782
      000186 23               [12]  284 	rl	a
      000187 F0               [24]  285 	movx	@dptr,a
                                    286 ;	src/usb.c:72: binstaddr = 16;
      000188 90 C7 88         [24]  287 	mov	dptr,#0xc788
      00018B 74 10            [12]  288 	mov	a,#0x10
      00018D F0               [24]  289 	movx	@dptr,a
                                    290 ;	src/usb.c:73: bin1addr  = 32;
      00018E 90 C7 89         [24]  291 	mov	dptr,#0xc789
      000191 23               [12]  292 	rl	a
      000192 F0               [24]  293 	movx	@dptr,a
                                    294 ;	src/usb.c:74: bin2addr  = 64;
      000193 90 C7 8A         [24]  295 	mov	dptr,#0xc78a
      000196 23               [12]  296 	rl	a
      000197 F0               [24]  297 	movx	@dptr,a
                                    298 ;	src/usb.c:75: out1bc    = 0xFF;
      000198 90 C7 C7         [24]  299 	mov	dptr,#0xc7c7
      00019B 74 FF            [12]  300 	mov	a,#0xff
      00019D F0               [24]  301 	movx	@dptr,a
                                    302 ;	src/usb.c:76: }
      00019E 22               [24]  303 	ret
                                    304 ;------------------------------------------------------------
                                    305 ;Allocation info for local variables in function 'usb_irq'
                                    306 ;------------------------------------------------------------
                                    307 ;	src/usb.c:79: void usb_irq() __interrupt(12)  __using(1)
                                    308 ;	-----------------------------------------
                                    309 ;	 function usb_irq
                                    310 ;	-----------------------------------------
      00019F                        311 _usb_irq:
                           00000F   312 	ar7 = 0x0f
                           00000E   313 	ar6 = 0x0e
                           00000D   314 	ar5 = 0x0d
                           00000C   315 	ar4 = 0x0c
                           00000B   316 	ar3 = 0x0b
                           00000A   317 	ar2 = 0x0a
                           000009   318 	ar1 = 0x09
                           000008   319 	ar0 = 0x08
      00019F C0 20            [24]  320 	push	bits
      0001A1 C0 E0            [24]  321 	push	acc
      0001A3 C0 F0            [24]  322 	push	b
      0001A5 C0 82            [24]  323 	push	dpl
      0001A7 C0 83            [24]  324 	push	dph
      0001A9 C0 07            [24]  325 	push	(0+7)
      0001AB C0 06            [24]  326 	push	(0+6)
      0001AD C0 05            [24]  327 	push	(0+5)
      0001AF C0 04            [24]  328 	push	(0+4)
      0001B1 C0 03            [24]  329 	push	(0+3)
      0001B3 C0 02            [24]  330 	push	(0+2)
      0001B5 C0 01            [24]  331 	push	(0+1)
      0001B7 C0 00            [24]  332 	push	(0+0)
      0001B9 C0 D0            [24]  333 	push	psw
      0001BB 75 D0 08         [24]  334 	mov	psw,#0x08
                                    335 ;	src/usb.c:83: switch (ivec) 
      0001BE 90 C7 A8         [24]  336 	mov	dptr,#0xc7a8
      0001C1 E0               [24]  337 	movx	a,@dptr
      0001C2 FF               [12]  338 	mov	r7,a
      0001C3 60 0A            [24]  339 	jz	00101$
      0001C5 BF 10 02         [24]  340 	cjne	r7,#0x10,00120$
      0001C8 80 16            [24]  341 	sjmp	00102$
      0001CA                        342 00120$:
                                    343 ;	src/usb.c:86: case 0x00:
      0001CA BF 24 4D         [24]  344 	cjne	r7,#0x24,00105$
      0001CD 80 22            [24]  345 	sjmp	00103$
      0001CF                        346 00101$:
                                    347 ;	src/usb.c:87: handle_setup_request();
      0001CF 75 D0 00         [24]  348 	mov	psw,#0x00
      0001D2 12 03 F0         [24]  349 	lcall	_handle_setup_request
      0001D5 75 D0 08         [24]  350 	mov	psw,#0x08
                                    351 ;	src/usb.c:88: usbirq = 0x01;
      0001D8 90 C7 AB         [24]  352 	mov	dptr,#0xc7ab
      0001DB 74 01            [12]  353 	mov	a,#0x01
      0001DD F0               [24]  354 	movx	@dptr,a
                                    355 ;	src/usb.c:89: break;
                                    356 ;	src/usb.c:92: case 0x10:
      0001DE 80 3A            [24]  357 	sjmp	00105$
      0001E0                        358 00102$:
                                    359 ;	src/usb.c:93: usb_reset_config();
      0001E0 75 D0 00         [24]  360 	mov	psw,#0x00
      0001E3 12 01 4C         [24]  361 	lcall	_usb_reset_config
      0001E6 75 D0 08         [24]  362 	mov	psw,#0x08
                                    363 ;	src/usb.c:94: usbirq = 0x10;
      0001E9 90 C7 AB         [24]  364 	mov	dptr,#0xc7ab
      0001EC 74 10            [12]  365 	mov	a,#0x10
      0001EE F0               [24]  366 	movx	@dptr,a
                                    367 ;	src/usb.c:95: break;
                                    368 ;	src/usb.c:98: case 0x24:
      0001EF 80 29            [24]  369 	sjmp	00105$
      0001F1                        370 00103$:
                                    371 ;	src/usb.c:99: handle_radio_request(out1buf[0], &out1buf[1]);
      0001F1 90 C6 40         [24]  372 	mov	dptr,#_out1buf
      0001F4 E0               [24]  373 	movx	a,@dptr
      0001F5 FF               [12]  374 	mov	r7,a
      0001F6 90 80 45         [24]  375 	mov	dptr,#_handle_radio_request_PARM_2
      0001F9 74 41            [12]  376 	mov	a,#(_out1buf + 0x0001)
      0001FB F0               [24]  377 	movx	@dptr,a
      0001FC 74 C6            [12]  378 	mov	a,#((_out1buf + 0x0001) >> 8)
      0001FE A3               [24]  379 	inc	dptr
      0001FF F0               [24]  380 	movx	@dptr,a
      000200 E4               [12]  381 	clr	a
      000201 A3               [24]  382 	inc	dptr
      000202 F0               [24]  383 	movx	@dptr,a
      000203 8F 82            [24]  384 	mov	dpl,r7
      000205 75 D0 00         [24]  385 	mov	psw,#0x00
      000208 12 0A 23         [24]  386 	lcall	_handle_radio_request
      00020B 75 D0 08         [24]  387 	mov	psw,#0x08
                                    388 ;	src/usb.c:100: out_irq = 0x02;
      00020E 90 C7 AA         [24]  389 	mov	dptr,#0xc7aa
      000211 74 02            [12]  390 	mov	a,#0x02
      000213 F0               [24]  391 	movx	@dptr,a
                                    392 ;	src/usb.c:101: out1bc = 0xFF;
      000214 90 C7 C7         [24]  393 	mov	dptr,#0xc7c7
      000217 74 FF            [12]  394 	mov	a,#0xff
      000219 F0               [24]  395 	movx	@dptr,a
                                    396 ;	src/usb.c:103: }
      00021A                        397 00105$:
                                    398 ;	src/usb.c:104: }
      00021A D0 D0            [24]  399 	pop	psw
      00021C D0 00            [24]  400 	pop	(0+0)
      00021E D0 01            [24]  401 	pop	(0+1)
      000220 D0 02            [24]  402 	pop	(0+2)
      000222 D0 03            [24]  403 	pop	(0+3)
      000224 D0 04            [24]  404 	pop	(0+4)
      000226 D0 05            [24]  405 	pop	(0+5)
      000228 D0 06            [24]  406 	pop	(0+6)
      00022A D0 07            [24]  407 	pop	(0+7)
      00022C D0 83            [24]  408 	pop	dph
      00022E D0 82            [24]  409 	pop	dpl
      000230 D0 F0            [24]  410 	pop	b
      000232 D0 E0            [24]  411 	pop	acc
      000234 D0 20            [24]  412 	pop	bits
      000236 32               [24]  413 	reti
                                    414 ;------------------------------------------------------------
                                    415 ;Allocation info for local variables in function 'write_device_string'
                                    416 ;------------------------------------------------------------
                                    417 ;sloc0                     Allocated with name '_write_device_string_sloc0_1_0'
                                    418 ;string                    Allocated with name '_write_device_string_string_65536_81'
                                    419 ;x                         Allocated with name '_write_device_string_x_65536_82'
                                    420 ;length                    Allocated with name '_write_device_string_length_65536_82'
                                    421 ;------------------------------------------------------------
                                    422 ;	src/usb.c:107: void write_device_string(const char * string)
                                    423 ;	-----------------------------------------
                                    424 ;	 function write_device_string
                                    425 ;	-----------------------------------------
      000237                        426 _write_device_string:
                           000007   427 	ar7 = 0x07
                           000006   428 	ar6 = 0x06
                           000005   429 	ar5 = 0x05
                           000004   430 	ar4 = 0x04
                           000003   431 	ar3 = 0x03
                           000002   432 	ar2 = 0x02
                           000001   433 	ar1 = 0x01
                           000000   434 	ar0 = 0x00
      000237 AF F0            [24]  435 	mov	r7,b
      000239 AE 83            [24]  436 	mov	r6,dph
      00023B E5 82            [12]  437 	mov	a,dpl
      00023D 90 80 0B         [24]  438 	mov	dptr,#_write_device_string_string_65536_81
      000240 F0               [24]  439 	movx	@dptr,a
      000241 EE               [12]  440 	mov	a,r6
      000242 A3               [24]  441 	inc	dptr
      000243 F0               [24]  442 	movx	@dptr,a
      000244 EF               [12]  443 	mov	a,r7
      000245 A3               [24]  444 	inc	dptr
      000246 F0               [24]  445 	movx	@dptr,a
                                    446 ;	src/usb.c:110: int length = strlen(string);
      000247 90 80 0B         [24]  447 	mov	dptr,#_write_device_string_string_65536_81
      00024A E0               [24]  448 	movx	a,@dptr
      00024B FD               [12]  449 	mov	r5,a
      00024C A3               [24]  450 	inc	dptr
      00024D E0               [24]  451 	movx	a,@dptr
      00024E FE               [12]  452 	mov	r6,a
      00024F A3               [24]  453 	inc	dptr
      000250 E0               [24]  454 	movx	a,@dptr
      000251 FF               [12]  455 	mov	r7,a
      000252 8D 82            [24]  456 	mov	dpl,r5
      000254 8E 83            [24]  457 	mov	dph,r6
      000256 8F F0            [24]  458 	mov	b,r7
      000258 12 16 B9         [24]  459 	lcall	_strlen
      00025B AE 82            [24]  460 	mov	r6,dpl
      00025D AF 83            [24]  461 	mov	r7,dph
                                    462 ;	src/usb.c:111: memset(in0buf+2, 0, 64);
      00025F 90 80 A9         [24]  463 	mov	dptr,#_memset_PARM_2
      000262 E4               [12]  464 	clr	a
      000263 F0               [24]  465 	movx	@dptr,a
      000264 90 80 AA         [24]  466 	mov	dptr,#_memset_PARM_3
      000267 74 40            [12]  467 	mov	a,#0x40
      000269 F0               [24]  468 	movx	@dptr,a
      00026A E4               [12]  469 	clr	a
      00026B A3               [24]  470 	inc	dptr
      00026C F0               [24]  471 	movx	@dptr,a
      00026D 90 C7 02         [24]  472 	mov	dptr,#(_in0buf + 0x0002)
      000270 75 F0 00         [24]  473 	mov	b,#0x00
      000273 C0 07            [24]  474 	push	ar7
      000275 C0 06            [24]  475 	push	ar6
      000277 12 16 76         [24]  476 	lcall	_memset
      00027A D0 06            [24]  477 	pop	ar6
      00027C D0 07            [24]  478 	pop	ar7
                                    479 ;	src/usb.c:112: in0buf[0] = 2+length*2;
      00027E 8E 04            [24]  480 	mov	ar4,r6
      000280 8F 05            [24]  481 	mov	ar5,r7
      000282 EC               [12]  482 	mov	a,r4
      000283 2C               [12]  483 	add	a,r4
      000284 FC               [12]  484 	mov	r4,a
      000285 0C               [12]  485 	inc	r4
      000286 0C               [12]  486 	inc	r4
      000287 90 C7 00         [24]  487 	mov	dptr,#_in0buf
      00028A EC               [12]  488 	mov	a,r4
      00028B F0               [24]  489 	movx	@dptr,a
                                    490 ;	src/usb.c:113: in0buf[1] = STRING_DESCRIPTOR;
      00028C 90 C7 01         [24]  491 	mov	dptr,#(_in0buf + 0x0001)
      00028F 74 03            [12]  492 	mov	a,#0x03
      000291 F0               [24]  493 	movx	@dptr,a
                                    494 ;	src/usb.c:114: for(x = 0; x < length; x++) in0buf[2+x*2] = string[x];
      000292 90 80 0B         [24]  495 	mov	dptr,#_write_device_string_string_65536_81
      000295 E0               [24]  496 	movx	a,@dptr
      000296 FB               [12]  497 	mov	r3,a
      000297 A3               [24]  498 	inc	dptr
      000298 E0               [24]  499 	movx	a,@dptr
      000299 FC               [12]  500 	mov	r4,a
      00029A A3               [24]  501 	inc	dptr
      00029B E0               [24]  502 	movx	a,@dptr
      00029C FD               [12]  503 	mov	r5,a
      00029D 79 00            [12]  504 	mov	r1,#0x00
      00029F 7A 00            [12]  505 	mov	r2,#0x00
      0002A1                        506 00103$:
      0002A1 C3               [12]  507 	clr	c
      0002A2 E9               [12]  508 	mov	a,r1
      0002A3 9E               [12]  509 	subb	a,r6
      0002A4 EA               [12]  510 	mov	a,r2
      0002A5 64 80            [12]  511 	xrl	a,#0x80
      0002A7 8F F0            [24]  512 	mov	b,r7
      0002A9 63 F0 80         [24]  513 	xrl	b,#0x80
      0002AC 95 F0            [12]  514 	subb	a,b
      0002AE 50 3B            [24]  515 	jnc	00101$
      0002B0 C0 06            [24]  516 	push	ar6
      0002B2 C0 07            [24]  517 	push	ar7
      0002B4 89 00            [24]  518 	mov	ar0,r1
      0002B6 E8               [12]  519 	mov	a,r0
      0002B7 28               [12]  520 	add	a,r0
      0002B8 F8               [12]  521 	mov	r0,a
      0002B9 08               [12]  522 	inc	r0
      0002BA 08               [12]  523 	inc	r0
      0002BB E8               [12]  524 	mov	a,r0
      0002BC 33               [12]  525 	rlc	a
      0002BD 95 E0            [12]  526 	subb	a,acc
      0002BF FF               [12]  527 	mov	r7,a
      0002C0 88 10            [24]  528 	mov	_write_device_string_sloc0_1_0,r0
      0002C2 74 C7            [12]  529 	mov	a,#(_in0buf >> 8)
      0002C4 2F               [12]  530 	add	a,r7
      0002C5 F5 11            [12]  531 	mov	(_write_device_string_sloc0_1_0 + 1),a
      0002C7 E9               [12]  532 	mov	a,r1
      0002C8 2B               [12]  533 	add	a,r3
      0002C9 F8               [12]  534 	mov	r0,a
      0002CA EA               [12]  535 	mov	a,r2
      0002CB 3C               [12]  536 	addc	a,r4
      0002CC FE               [12]  537 	mov	r6,a
      0002CD 8D 07            [24]  538 	mov	ar7,r5
      0002CF 88 82            [24]  539 	mov	dpl,r0
      0002D1 8E 83            [24]  540 	mov	dph,r6
      0002D3 8F F0            [24]  541 	mov	b,r7
      0002D5 12 16 D1         [24]  542 	lcall	__gptrget
      0002D8 F8               [12]  543 	mov	r0,a
      0002D9 85 10 82         [24]  544 	mov	dpl,_write_device_string_sloc0_1_0
      0002DC 85 11 83         [24]  545 	mov	dph,(_write_device_string_sloc0_1_0 + 1)
      0002DF F0               [24]  546 	movx	@dptr,a
      0002E0 09               [12]  547 	inc	r1
      0002E1 B9 00 01         [24]  548 	cjne	r1,#0x00,00117$
      0002E4 0A               [12]  549 	inc	r2
      0002E5                        550 00117$:
      0002E5 D0 07            [24]  551 	pop	ar7
      0002E7 D0 06            [24]  552 	pop	ar6
      0002E9 80 B6            [24]  553 	sjmp	00103$
      0002EB                        554 00101$:
                                    555 ;	src/usb.c:115: in0bc = in0buf[0];
      0002EB 90 C7 00         [24]  556 	mov	dptr,#_in0buf
      0002EE E0               [24]  557 	movx	a,@dptr
      0002EF 90 C7 B5         [24]  558 	mov	dptr,#0xc7b5
      0002F2 F0               [24]  559 	movx	@dptr,a
                                    560 ;	src/usb.c:116: }
      0002F3 22               [24]  561 	ret
                                    562 ;------------------------------------------------------------
                                    563 ;Allocation info for local variables in function 'write_descriptor'
                                    564 ;------------------------------------------------------------
                                    565 ;desc_len                  Allocated with name '_write_descriptor_desc_len_65536_84'
                                    566 ;------------------------------------------------------------
                                    567 ;	src/usb.c:119: bool write_descriptor()
                                    568 ;	-----------------------------------------
                                    569 ;	 function write_descriptor
                                    570 ;	-----------------------------------------
      0002F4                        571 _write_descriptor:
                                    572 ;	src/usb.c:121: uint8_t desc_len = request->wLength;
      0002F4 90 80 B7         [24]  573 	mov	dptr,#_request
      0002F7 E0               [24]  574 	movx	a,@dptr
      0002F8 FE               [12]  575 	mov	r6,a
      0002F9 A3               [24]  576 	inc	dptr
      0002FA E0               [24]  577 	movx	a,@dptr
      0002FB FF               [12]  578 	mov	r7,a
      0002FC 74 06            [12]  579 	mov	a,#0x06
      0002FE 2E               [12]  580 	add	a,r6
      0002FF F5 82            [12]  581 	mov	dpl,a
      000301 E4               [12]  582 	clr	a
      000302 3F               [12]  583 	addc	a,r7
      000303 F5 83            [12]  584 	mov	dph,a
      000305 E0               [24]  585 	movx	a,@dptr
      000306 FD               [12]  586 	mov	r5,a
      000307 90 80 0E         [24]  587 	mov	dptr,#_write_descriptor_desc_len_65536_84
      00030A F0               [24]  588 	movx	@dptr,a
                                    589 ;	src/usb.c:123: switch(request->wValue >> 8)
      00030B 8E 82            [24]  590 	mov	dpl,r6
      00030D 8F 83            [24]  591 	mov	dph,r7
      00030F A3               [24]  592 	inc	dptr
      000310 A3               [24]  593 	inc	dptr
      000311 E0               [24]  594 	movx	a,@dptr
      000312 A3               [24]  595 	inc	dptr
      000313 E0               [24]  596 	movx	a,@dptr
      000314 FE               [12]  597 	mov	r6,a
      000315 7F 00            [12]  598 	mov	r7,#0x00
      000317 8E 03            [24]  599 	mov	ar3,r6
      000319 8F 04            [24]  600 	mov	ar4,r7
      00031B BB 01 05         [24]  601 	cjne	r3,#0x01,00131$
      00031E BC 00 02         [24]  602 	cjne	r4,#0x00,00131$
      000321 80 14            [24]  603 	sjmp	00101$
      000323                        604 00131$:
      000323 BE 02 05         [24]  605 	cjne	r6,#0x02,00132$
      000326 BF 00 02         [24]  606 	cjne	r7,#0x00,00132$
      000329 80 4F            [24]  607 	sjmp	00104$
      00032B                        608 00132$:
      00032B BE 03 06         [24]  609 	cjne	r6,#0x03,00133$
      00032E BF 00 03         [24]  610 	cjne	r7,#0x00,00133$
      000331 02 03 C6         [24]  611 	ljmp	00107$
      000334                        612 00133$:
      000334 02 03 EC         [24]  613 	ljmp	00108$
                                    614 ;	src/usb.c:126: case DEVICE_DESCRIPTOR:
      000337                        615 00101$:
                                    616 ;	src/usb.c:127: if(desc_len > device_descriptor.bLength) desc_len = device_descriptor.bLength;
      000337 90 16 F1         [24]  617 	mov	dptr,#_device_descriptor
      00033A E4               [12]  618 	clr	a
      00033B 93               [24]  619 	movc	a,@a+dptr
      00033C FF               [12]  620 	mov	r7,a
      00033D C3               [12]  621 	clr	c
      00033E 9D               [12]  622 	subb	a,r5
      00033F 50 05            [24]  623 	jnc	00103$
      000341 90 80 0E         [24]  624 	mov	dptr,#_write_descriptor_desc_len_65536_84
      000344 EF               [12]  625 	mov	a,r7
      000345 F0               [24]  626 	movx	@dptr,a
      000346                        627 00103$:
                                    628 ;	src/usb.c:128: memcpy(in0buf, &device_descriptor, desc_len);
      000346 90 80 0E         [24]  629 	mov	dptr,#_write_descriptor_desc_len_65536_84
      000349 E0               [24]  630 	movx	a,@dptr
      00034A FF               [12]  631 	mov	r7,a
      00034B FC               [12]  632 	mov	r4,a
      00034C 7E 00            [12]  633 	mov	r6,#0x00
      00034E 90 80 A1         [24]  634 	mov	dptr,#___memcpy_PARM_2
      000351 74 F1            [12]  635 	mov	a,#_device_descriptor
      000353 F0               [24]  636 	movx	@dptr,a
      000354 74 16            [12]  637 	mov	a,#(_device_descriptor >> 8)
      000356 A3               [24]  638 	inc	dptr
      000357 F0               [24]  639 	movx	@dptr,a
      000358 74 80            [12]  640 	mov	a,#0x80
      00035A A3               [24]  641 	inc	dptr
      00035B F0               [24]  642 	movx	@dptr,a
      00035C 90 80 A4         [24]  643 	mov	dptr,#___memcpy_PARM_3
      00035F EC               [12]  644 	mov	a,r4
      000360 F0               [24]  645 	movx	@dptr,a
      000361 EE               [12]  646 	mov	a,r6
      000362 A3               [24]  647 	inc	dptr
      000363 F0               [24]  648 	movx	@dptr,a
      000364 90 C7 00         [24]  649 	mov	dptr,#_in0buf
      000367 75 F0 00         [24]  650 	mov	b,#0x00
      00036A C0 07            [24]  651 	push	ar7
      00036C 12 16 02         [24]  652 	lcall	___memcpy
      00036F D0 07            [24]  653 	pop	ar7
                                    654 ;	src/usb.c:129: in0bc = desc_len;
      000371 90 C7 B5         [24]  655 	mov	dptr,#0xc7b5
      000374 EF               [12]  656 	mov	a,r7
      000375 F0               [24]  657 	movx	@dptr,a
                                    658 ;	src/usb.c:130: return true;
      000376 75 82 01         [24]  659 	mov	dpl,#0x01
      000379 22               [24]  660 	ret
                                    661 ;	src/usb.c:133: case CONFIGURATION_DESCRIPTOR:
      00037A                        662 00104$:
                                    663 ;	src/usb.c:134: if(desc_len > configuration_descriptor.wTotalLength) desc_len = configuration_descriptor.wTotalLength;
      00037A 90 17 05         [24]  664 	mov	dptr,#(_configuration_descriptor + 0x0002)
      00037D E4               [12]  665 	clr	a
      00037E 93               [24]  666 	movc	a,@a+dptr
      00037F FE               [12]  667 	mov	r6,a
      000380 A3               [24]  668 	inc	dptr
      000381 E4               [12]  669 	clr	a
      000382 93               [24]  670 	movc	a,@a+dptr
      000383 FF               [12]  671 	mov	r7,a
      000384 7C 00            [12]  672 	mov	r4,#0x00
      000386 C3               [12]  673 	clr	c
      000387 EE               [12]  674 	mov	a,r6
      000388 9D               [12]  675 	subb	a,r5
      000389 EF               [12]  676 	mov	a,r7
      00038A 9C               [12]  677 	subb	a,r4
      00038B 50 05            [24]  678 	jnc	00106$
      00038D 90 80 0E         [24]  679 	mov	dptr,#_write_descriptor_desc_len_65536_84
      000390 EE               [12]  680 	mov	a,r6
      000391 F0               [24]  681 	movx	@dptr,a
      000392                        682 00106$:
                                    683 ;	src/usb.c:135: memcpy(in0buf, &configuration_descriptor, desc_len);
      000392 90 80 0E         [24]  684 	mov	dptr,#_write_descriptor_desc_len_65536_84
      000395 E0               [24]  685 	movx	a,@dptr
      000396 FF               [12]  686 	mov	r7,a
      000397 FD               [12]  687 	mov	r5,a
      000398 7E 00            [12]  688 	mov	r6,#0x00
      00039A 90 80 A1         [24]  689 	mov	dptr,#___memcpy_PARM_2
      00039D 74 03            [12]  690 	mov	a,#_configuration_descriptor
      00039F F0               [24]  691 	movx	@dptr,a
      0003A0 74 17            [12]  692 	mov	a,#(_configuration_descriptor >> 8)
      0003A2 A3               [24]  693 	inc	dptr
      0003A3 F0               [24]  694 	movx	@dptr,a
      0003A4 74 80            [12]  695 	mov	a,#0x80
      0003A6 A3               [24]  696 	inc	dptr
      0003A7 F0               [24]  697 	movx	@dptr,a
      0003A8 90 80 A4         [24]  698 	mov	dptr,#___memcpy_PARM_3
      0003AB ED               [12]  699 	mov	a,r5
      0003AC F0               [24]  700 	movx	@dptr,a
      0003AD EE               [12]  701 	mov	a,r6
      0003AE A3               [24]  702 	inc	dptr
      0003AF F0               [24]  703 	movx	@dptr,a
      0003B0 90 C7 00         [24]  704 	mov	dptr,#_in0buf
      0003B3 75 F0 00         [24]  705 	mov	b,#0x00
      0003B6 C0 07            [24]  706 	push	ar7
      0003B8 12 16 02         [24]  707 	lcall	___memcpy
      0003BB D0 07            [24]  708 	pop	ar7
                                    709 ;	src/usb.c:136: in0bc = desc_len;
      0003BD 90 C7 B5         [24]  710 	mov	dptr,#0xc7b5
      0003C0 EF               [12]  711 	mov	a,r7
      0003C1 F0               [24]  712 	movx	@dptr,a
                                    713 ;	src/usb.c:137: return true;
      0003C2 75 82 01         [24]  714 	mov	dpl,#0x01
                                    715 ;	src/usb.c:141: case STRING_DESCRIPTOR:
      0003C5 22               [24]  716 	ret
      0003C6                        717 00107$:
                                    718 ;	src/usb.c:142: write_device_string(device_strings[setupbuf[2]]);
      0003C6 90 C7 EA         [24]  719 	mov	dptr,#(_setupbuf + 0x0002)
      0003C9 E0               [24]  720 	movx	a,@dptr
      0003CA 75 F0 02         [24]  721 	mov	b,#0x02
      0003CD A4               [48]  722 	mul	ab
      0003CE 24 B9            [12]  723 	add	a,#_device_strings
      0003D0 F5 82            [12]  724 	mov	dpl,a
      0003D2 74 80            [12]  725 	mov	a,#(_device_strings >> 8)
      0003D4 35 F0            [12]  726 	addc	a,b
      0003D6 F5 83            [12]  727 	mov	dph,a
      0003D8 E0               [24]  728 	movx	a,@dptr
      0003D9 FE               [12]  729 	mov	r6,a
      0003DA A3               [24]  730 	inc	dptr
      0003DB E0               [24]  731 	movx	a,@dptr
      0003DC FF               [12]  732 	mov	r7,a
      0003DD 7D 80            [12]  733 	mov	r5,#0x80
      0003DF 8E 82            [24]  734 	mov	dpl,r6
      0003E1 8F 83            [24]  735 	mov	dph,r7
      0003E3 8D F0            [24]  736 	mov	b,r5
      0003E5 12 02 37         [24]  737 	lcall	_write_device_string
                                    738 ;	src/usb.c:143: return true;   
      0003E8 75 82 01         [24]  739 	mov	dpl,#0x01
                                    740 ;	src/usb.c:144: }  
      0003EB 22               [24]  741 	ret
      0003EC                        742 00108$:
                                    743 ;	src/usb.c:147: return false;
      0003EC 75 82 00         [24]  744 	mov	dpl,#0x00
                                    745 ;	src/usb.c:148: }
      0003EF 22               [24]  746 	ret
                                    747 ;------------------------------------------------------------
                                    748 ;Allocation info for local variables in function 'handle_setup_request'
                                    749 ;------------------------------------------------------------
                                    750 ;handled                   Allocated with name '_handle_setup_request_handled_65536_86'
                                    751 ;------------------------------------------------------------
                                    752 ;	src/usb.c:151: void handle_setup_request()
                                    753 ;	-----------------------------------------
                                    754 ;	 function handle_setup_request
                                    755 ;	-----------------------------------------
      0003F0                        756 _handle_setup_request:
                                    757 ;	src/usb.c:153: bool handled = false;
      0003F0 90 80 0F         [24]  758 	mov	dptr,#_handle_setup_request_handled_65536_86
      0003F3 E4               [12]  759 	clr	a
      0003F4 F0               [24]  760 	movx	@dptr,a
                                    761 ;	src/usb.c:154: switch(request->bRequest)
      0003F5 90 80 B7         [24]  762 	mov	dptr,#_request
      0003F8 E0               [24]  763 	movx	a,@dptr
      0003F9 FE               [12]  764 	mov	r6,a
      0003FA A3               [24]  765 	inc	dptr
      0003FB E0               [24]  766 	movx	a,@dptr
      0003FC FF               [12]  767 	mov	r7,a
      0003FD 8E 82            [24]  768 	mov	dpl,r6
      0003FF 8F 83            [24]  769 	mov	dph,r7
      000401 A3               [24]  770 	inc	dptr
      000402 E0               [24]  771 	movx	a,@dptr
      000403 FD               [12]  772 	mov	r5,a
      000404 60 6B            [24]  773 	jz	00110$
      000406 BD 05 02         [24]  774 	cjne	r5,#0x05,00164$
      000409 80 25            [24]  775 	sjmp	00104$
      00040B                        776 00164$:
      00040B BD 06 02         [24]  777 	cjne	r5,#0x06,00165$
      00040E 80 0D            [24]  778 	sjmp	00101$
      000410                        779 00165$:
      000410 BD 08 02         [24]  780 	cjne	r5,#0x08,00166$
      000413 80 47            [24]  781 	sjmp	00109$
      000415                        782 00166$:
      000415 BD 09 02         [24]  783 	cjne	r5,#0x09,00167$
      000418 80 1F            [24]  784 	sjmp	00105$
      00041A                        785 00167$:
      00041A 02 04 B4         [24]  786 	ljmp	00117$
                                    787 ;	src/usb.c:157: case GET_DESCRIPTOR:
      00041D                        788 00101$:
                                    789 ;	src/usb.c:158: if(write_descriptor()) handled = true;
      00041D 12 02 F4         [24]  790 	lcall	_write_descriptor
      000420 E5 82            [12]  791 	mov	a,dpl
      000422 70 03            [24]  792 	jnz	00168$
      000424 02 04 B4         [24]  793 	ljmp	00117$
      000427                        794 00168$:
      000427 90 80 0F         [24]  795 	mov	dptr,#_handle_setup_request_handled_65536_86
      00042A 74 01            [12]  796 	mov	a,#0x01
      00042C F0               [24]  797 	movx	@dptr,a
                                    798 ;	src/usb.c:159: break;
      00042D 02 04 B4         [24]  799 	ljmp	00117$
                                    800 ;	src/usb.c:162: case SET_ADDRESS:
      000430                        801 00104$:
                                    802 ;	src/usb.c:163: handled = true;
      000430 90 80 0F         [24]  803 	mov	dptr,#_handle_setup_request_handled_65536_86
      000433 74 01            [12]  804 	mov	a,#0x01
      000435 F0               [24]  805 	movx	@dptr,a
                                    806 ;	src/usb.c:164: break;
      000436 02 04 B4         [24]  807 	ljmp	00117$
                                    808 ;	src/usb.c:167: case SET_CONFIGURATION:   
      000439                        809 00105$:
                                    810 ;	src/usb.c:168: if (request->wValue == 0) configured = false; // Not configured, drop back to powered state
      000439 8E 82            [24]  811 	mov	dpl,r6
      00043B 8F 83            [24]  812 	mov	dph,r7
      00043D A3               [24]  813 	inc	dptr
      00043E A3               [24]  814 	inc	dptr
      00043F E0               [24]  815 	movx	a,@dptr
      000440 FC               [12]  816 	mov	r4,a
      000441 A3               [24]  817 	inc	dptr
      000442 E0               [24]  818 	movx	a,@dptr
      000443 FD               [12]  819 	mov	r5,a
      000444 4C               [12]  820 	orl	a,r4
      000445 70 07            [24]  821 	jnz	00107$
      000447 90 80 0A         [24]  822 	mov	dptr,#_configured
      00044A E4               [12]  823 	clr	a
      00044B F0               [24]  824 	movx	@dptr,a
      00044C 80 06            [24]  825 	sjmp	00108$
      00044E                        826 00107$:
                                    827 ;	src/usb.c:169: else configured = true;                       // Configured
      00044E 90 80 0A         [24]  828 	mov	dptr,#_configured
      000451 74 01            [12]  829 	mov	a,#0x01
      000453 F0               [24]  830 	movx	@dptr,a
      000454                        831 00108$:
                                    832 ;	src/usb.c:170: handled = true;
      000454 90 80 0F         [24]  833 	mov	dptr,#_handle_setup_request_handled_65536_86
      000457 74 01            [12]  834 	mov	a,#0x01
      000459 F0               [24]  835 	movx	@dptr,a
                                    836 ;	src/usb.c:171: break;
                                    837 ;	src/usb.c:174: case GET_CONFIGURATION:
      00045A 80 58            [24]  838 	sjmp	00117$
      00045C                        839 00109$:
                                    840 ;	src/usb.c:175: in0buf[0] = configured;
      00045C 90 80 0A         [24]  841 	mov	dptr,#_configured
      00045F E0               [24]  842 	movx	a,@dptr
      000460 FD               [12]  843 	mov	r5,a
      000461 90 C7 00         [24]  844 	mov	dptr,#_in0buf
      000464 F0               [24]  845 	movx	@dptr,a
                                    846 ;	src/usb.c:176: in0bc = 1;
      000465 90 C7 B5         [24]  847 	mov	dptr,#0xc7b5
      000468 74 01            [12]  848 	mov	a,#0x01
      00046A F0               [24]  849 	movx	@dptr,a
                                    850 ;	src/usb.c:177: handled = true;
      00046B 90 80 0F         [24]  851 	mov	dptr,#_handle_setup_request_handled_65536_86
      00046E F0               [24]  852 	movx	@dptr,a
                                    853 ;	src/usb.c:178: break;
                                    854 ;	src/usb.c:181: case GET_STATUS:
      00046F 80 43            [24]  855 	sjmp	00117$
      000471                        856 00110$:
                                    857 ;	src/usb.c:184: if (request->bmRequestType == 0x82)
      000471 8E 82            [24]  858 	mov	dpl,r6
      000473 8F 83            [24]  859 	mov	dph,r7
      000475 E0               [24]  860 	movx	a,@dptr
      000476 FE               [12]  861 	mov	r6,a
      000477 BE 82 26         [24]  862 	cjne	r6,#0x82,00115$
                                    863 ;	src/usb.c:186: if ((setupbuf[4] & 0x80) == 0x80) in0buf[0] = in1cs;
      00047A 90 C7 EC         [24]  864 	mov	dptr,#(_setupbuf + 0x0004)
      00047D E0               [24]  865 	movx	a,@dptr
      00047E FF               [12]  866 	mov	r7,a
      00047F 53 07 80         [24]  867 	anl	ar7,#0x80
      000482 7E 00            [12]  868 	mov	r6,#0x00
      000484 BF 80 0E         [24]  869 	cjne	r7,#0x80,00112$
      000487 BE 00 0B         [24]  870 	cjne	r6,#0x00,00112$
      00048A 90 C7 B6         [24]  871 	mov	dptr,#0xc7b6
      00048D E0               [24]  872 	movx	a,@dptr
      00048E FF               [12]  873 	mov	r7,a
      00048F 90 C7 00         [24]  874 	mov	dptr,#_in0buf
      000492 F0               [24]  875 	movx	@dptr,a
      000493 80 14            [24]  876 	sjmp	00116$
      000495                        877 00112$:
                                    878 ;	src/usb.c:187: else in0buf[0] = out1cs; 
      000495 90 C7 C6         [24]  879 	mov	dptr,#0xc7c6
      000498 E0               [24]  880 	movx	a,@dptr
      000499 FF               [12]  881 	mov	r7,a
      00049A 90 C7 00         [24]  882 	mov	dptr,#_in0buf
      00049D F0               [24]  883 	movx	@dptr,a
      00049E 80 09            [24]  884 	sjmp	00116$
      0004A0                        885 00115$:
                                    886 ;	src/usb.c:194: in0buf[0] = 0;
      0004A0 90 C7 00         [24]  887 	mov	dptr,#_in0buf
      0004A3 E4               [12]  888 	clr	a
      0004A4 F0               [24]  889 	movx	@dptr,a
                                    890 ;	src/usb.c:195: in0buf[1] = 0;
      0004A5 90 C7 01         [24]  891 	mov	dptr,#(_in0buf + 0x0001)
      0004A8 F0               [24]  892 	movx	@dptr,a
      0004A9                        893 00116$:
                                    894 ;	src/usb.c:198: in0bc = 2;
      0004A9 90 C7 B5         [24]  895 	mov	dptr,#0xc7b5
      0004AC 74 02            [12]  896 	mov	a,#0x02
      0004AE F0               [24]  897 	movx	@dptr,a
                                    898 ;	src/usb.c:199: handled = true;
      0004AF 90 80 0F         [24]  899 	mov	dptr,#_handle_setup_request_handled_65536_86
      0004B2 14               [12]  900 	dec	a
      0004B3 F0               [24]  901 	movx	@dptr,a
                                    902 ;	src/usb.c:201: }
      0004B4                        903 00117$:
                                    904 ;	src/usb.c:204: if(handled) ep0cs = 0x02; // hsnak
      0004B4 90 80 0F         [24]  905 	mov	dptr,#_handle_setup_request_handled_65536_86
      0004B7 E0               [24]  906 	movx	a,@dptr
      0004B8 60 07            [24]  907 	jz	00119$
      0004BA 90 C7 B4         [24]  908 	mov	dptr,#0xc7b4
      0004BD 74 02            [12]  909 	mov	a,#0x02
      0004BF F0               [24]  910 	movx	@dptr,a
      0004C0 22               [24]  911 	ret
      0004C1                        912 00119$:
                                    913 ;	src/usb.c:205: else ep0cs = 0x01; // ep0stall
      0004C1 90 C7 B4         [24]  914 	mov	dptr,#0xc7b4
      0004C4 74 01            [12]  915 	mov	a,#0x01
      0004C6 F0               [24]  916 	movx	@dptr,a
                                    917 ;	src/usb.c:206: }
      0004C7 22               [24]  918 	ret
                                    919 	.area CSEG    (CODE)
                                    920 	.area CONST   (CODE)
                                    921 	.area XINIT   (CODE)
      001746                        922 __xinit__nordic_bootloader:
      001746 00 78                  923 	.byte #0x00,#0x78
      001748                        924 __xinit__logitech_bootloader:
      001748 00 74                  925 	.byte #0x00,#0x74
      00174A                        926 __xinit__request:
      00174A E8 C7                  927 	.byte _setupbuf, (_setupbuf >> 8)
                                    928 	.area CABS    (ABS,CODE)
