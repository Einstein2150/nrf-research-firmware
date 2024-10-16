                                      1 ;--------------------------------------------------------
                                      2 ; File Created by SDCC : free open source ANSI-C Compiler
                                      3 ; Version 4.0.0 #11528 (Mac OS X x86_64)
                                      4 ;--------------------------------------------------------
                                      5 	.module radio
                                      6 	.optsdcc -mmcs51 --model-large
                                      7 	
                                      8 ;--------------------------------------------------------
                                      9 ; Public variables in this module
                                     10 ;--------------------------------------------------------
                                     11 	.globl _spi_transfer
                                     12 	.globl ___memcpy
                                     13 	.globl _RFRDY
                                     14 	.globl _rfcsn
                                     15 	.globl _rfce
                                     16 	.globl _ien1
                                     17 	.globl _ien0
                                     18 	.globl _REGXC
                                     19 	.globl _REGXL
                                     20 	.globl _REGXH
                                     21 	.globl _TICKDV
                                     22 	.globl _RFDAT
                                     23 	.globl _P0DIR
                                     24 	.globl _P0
                                     25 	.globl _AESIA1
                                     26 	.globl _AESIV
                                     27 	.globl _usbcon
                                     28 	.globl _rfcon
                                     29 	.globl _rfctl
                                     30 	.globl _handle_radio_request_PARM_2
                                     31 	.globl _crc_update_PARM_3
                                     32 	.globl _crc_update_PARM_2
                                     33 	.globl _write_register_byte_PARM_2
                                     34 	.globl _spi_read_PARM_3
                                     35 	.globl _spi_read_PARM_2
                                     36 	.globl _spi_write_PARM_3
                                     37 	.globl _spi_write_PARM_2
                                     38 	.globl _configure_phy_PARM_3
                                     39 	.globl _configure_phy_PARM_2
                                     40 	.globl _configure_mac_PARM_3
                                     41 	.globl _configure_mac_PARM_2
                                     42 	.globl _configure_address_PARM_2
                                     43 	.globl _enter_promiscuous_mode_generic_PARM_4
                                     44 	.globl _enter_promiscuous_mode_generic_PARM_3
                                     45 	.globl _enter_promiscuous_mode_generic_PARM_2
                                     46 	.globl _enter_promiscuous_mode_PARM_2
                                     47 	.globl _setupbuf
                                     48 	.globl _out1buf
                                     49 	.globl _in1buf
                                     50 	.globl _in0buf
                                     51 	.globl _enter_promiscuous_mode
                                     52 	.globl _enter_promiscuous_mode_generic
                                     53 	.globl _configure_address
                                     54 	.globl _configure_mac
                                     55 	.globl _configure_phy
                                     56 	.globl _spi_write
                                     57 	.globl _spi_read
                                     58 	.globl _write_register_byte
                                     59 	.globl _read_register_byte
                                     60 	.globl _crc_update
                                     61 	.globl _handle_radio_request
                                     62 ;--------------------------------------------------------
                                     63 ; special function registers
                                     64 ;--------------------------------------------------------
                                     65 	.area RSEG    (ABS,DATA)
      000000                         66 	.org 0x0000
                           0000E6    67 _rfctl	=	0x00e6
                           000090    68 _rfcon	=	0x0090
                           0000A0    69 _usbcon	=	0x00a0
                           0000F2    70 _AESIV	=	0x00f2
                           0000F5    71 _AESIA1	=	0x00f5
                           000080    72 _P0	=	0x0080
                           000094    73 _P0DIR	=	0x0094
                           0000E5    74 _RFDAT	=	0x00e5
                           0000AB    75 _TICKDV	=	0x00ab
                           0000AB    76 _REGXH	=	0x00ab
                           0000AC    77 _REGXL	=	0x00ac
                           0000AD    78 _REGXC	=	0x00ad
                           0000A8    79 _ien0	=	0x00a8
                           0000B8    80 _ien1	=	0x00b8
                                     81 ;--------------------------------------------------------
                                     82 ; special function bits
                                     83 ;--------------------------------------------------------
                                     84 	.area RSEG    (ABS,DATA)
      000000                         85 	.org 0x0000
                           000090    86 _rfce	=	0x0090
                           000091    87 _rfcsn	=	0x0091
                           0000C0    88 _RFRDY	=	0x00c0
                                     89 ;--------------------------------------------------------
                                     90 ; overlayable register banks
                                     91 ;--------------------------------------------------------
                                     92 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                         93 	.ds 8
                                     94 ;--------------------------------------------------------
                                     95 ; internal ram data
                                     96 ;--------------------------------------------------------
                                     97 	.area DSEG    (DATA)
      000021                         98 _enter_promiscuous_mode_sloc0_1_0:
      000021                         99 	.ds 3
      000024                        100 _enter_promiscuous_mode_sloc1_1_0:
      000024                        101 	.ds 2
      000026                        102 _enter_promiscuous_mode_generic_sloc0_1_0:
      000026                        103 	.ds 3
      000029                        104 _enter_promiscuous_mode_generic_sloc1_1_0:
      000029                        105 	.ds 2
      00002B                        106 _spi_read_sloc0_1_0:
      00002B                        107 	.ds 3
      00002E                        108 _handle_radio_request_sloc0_1_0:
      00002E                        109 	.ds 1
      00002F                        110 _handle_radio_request_sloc1_1_0:
      00002F                        111 	.ds 3
      000032                        112 _handle_radio_request_sloc2_1_0:
      000032                        113 	.ds 2
                                    114 ;--------------------------------------------------------
                                    115 ; overlayable items in internal ram 
                                    116 ;--------------------------------------------------------
                                    117 ;--------------------------------------------------------
                                    118 ; indirectly addressable internal ram data
                                    119 ;--------------------------------------------------------
                                    120 	.area ISEG    (DATA)
                                    121 ;--------------------------------------------------------
                                    122 ; absolute internal ram data
                                    123 ;--------------------------------------------------------
                                    124 	.area IABS    (ABS,DATA)
                                    125 	.area IABS    (ABS,DATA)
                                    126 ;--------------------------------------------------------
                                    127 ; bit data
                                    128 ;--------------------------------------------------------
                                    129 	.area BSEG    (BIT)
                                    130 ;--------------------------------------------------------
                                    131 ; paged external ram data
                                    132 ;--------------------------------------------------------
                                    133 	.area PSEG    (PAG,XDATA)
                                    134 ;--------------------------------------------------------
                                    135 ; external ram data
                                    136 ;--------------------------------------------------------
                                    137 	.area XSEG    (XDATA)
                           00C700   138 _in0buf	=	0xc700
                           00C680   139 _in1buf	=	0xc680
                           00C640   140 _out1buf	=	0xc640
                           00C7E8   141 _setupbuf	=	0xc7e8
      008010                        142 _configured:
      008010                        143 	.ds 1
      008011                        144 _radio_mode:
      008011                        145 	.ds 1
      008012                        146 _pm_prefix_length:
      008012                        147 	.ds 2
      008014                        148 _pm_prefix:
      008014                        149 	.ds 5
      008019                        150 _pm_payload_length:
      008019                        151 	.ds 1
      00801A                        152 _enter_promiscuous_mode_PARM_2:
      00801A                        153 	.ds 1
      00801B                        154 _enter_promiscuous_mode_prefix_65536_38:
      00801B                        155 	.ds 3
      00801E                        156 _enter_promiscuous_mode_address_131072_41:
      00801E                        157 	.ds 2
      008020                        158 _enter_promiscuous_mode_generic_PARM_2:
      008020                        159 	.ds 1
      008021                        160 _enter_promiscuous_mode_generic_PARM_3:
      008021                        161 	.ds 1
      008022                        162 _enter_promiscuous_mode_generic_PARM_4:
      008022                        163 	.ds 1
      008023                        164 _enter_promiscuous_mode_generic_prefix_65536_42:
      008023                        165 	.ds 3
      008026                        166 _enter_promiscuous_mode_generic_address_131072_45:
      008026                        167 	.ds 2
      008028                        168 _configure_address_PARM_2:
      008028                        169 	.ds 1
      008029                        170 _configure_address_address_65536_47:
      008029                        171 	.ds 3
      00802C                        172 _configure_mac_PARM_2:
      00802C                        173 	.ds 1
      00802D                        174 _configure_mac_PARM_3:
      00802D                        175 	.ds 1
      00802E                        176 _configure_mac_feature_65536_49:
      00802E                        177 	.ds 1
      00802F                        178 _configure_phy_PARM_2:
      00802F                        179 	.ds 1
      008030                        180 _configure_phy_PARM_3:
      008030                        181 	.ds 1
      008031                        182 _configure_phy_config_65536_51:
      008031                        183 	.ds 1
      008032                        184 _spi_transfer_byte_65536_53:
      008032                        185 	.ds 1
      008033                        186 _spi_write_PARM_2:
      008033                        187 	.ds 3
      008036                        188 _spi_write_PARM_3:
      008036                        189 	.ds 1
      008037                        190 _spi_write_command_65536_55:
      008037                        191 	.ds 1
      008038                        192 _spi_read_PARM_2:
      008038                        193 	.ds 3
      00803B                        194 _spi_read_PARM_3:
      00803B                        195 	.ds 1
      00803C                        196 _spi_read_command_65536_58:
      00803C                        197 	.ds 1
      00803D                        198 _write_register_byte_PARM_2:
      00803D                        199 	.ds 1
      00803E                        200 _write_register_byte_reg_65536_61:
      00803E                        201 	.ds 1
      00803F                        202 _read_register_byte_reg_65536_63:
      00803F                        203 	.ds 1
      008040                        204 _read_register_byte_value_65536_64:
      008040                        205 	.ds 1
      008041                        206 _crc_update_PARM_2:
      008041                        207 	.ds 1
      008042                        208 _crc_update_PARM_3:
      008042                        209 	.ds 1
      008043                        210 _crc_update_crc_65536_65:
      008043                        211 	.ds 2
      008045                        212 _handle_radio_request_PARM_2:
      008045                        213 	.ds 3
      008048                        214 _handle_radio_request_request_65536_67:
      008048                        215 	.ds 1
      008049                        216 _handle_radio_request_command_131072_70:
      008049                        217 	.ds 9
      008052                        218 _handle_radio_request_value_131072_79:
      008052                        219 	.ds 1
      008053                        220 _handle_radio_request_crc_262144_84:
      008053                        221 	.ds 2
      008055                        222 _handle_radio_request_crc_given_262144_84:
      008055                        223 	.ds 2
      008057                        224 _handle_radio_request_payload_262144_84:
      008057                        225 	.ds 37
      00807C                        226 _handle_radio_request_payload_262144_95:
      00807C                        227 	.ds 37
                                    228 ;--------------------------------------------------------
                                    229 ; absolute external ram data
                                    230 ;--------------------------------------------------------
                                    231 	.area XABS    (ABS,XDATA)
                                    232 ;--------------------------------------------------------
                                    233 ; external initialized ram data
                                    234 ;--------------------------------------------------------
                                    235 	.area XISEG   (XDATA)
      0080BF                        236 _nordic_bootloader:
      0080BF                        237 	.ds 2
      0080C1                        238 _logitech_bootloader:
      0080C1                        239 	.ds 2
      0080C3                        240 _promiscuous_address:
      0080C3                        241 	.ds 2
                                    242 	.area HOME    (CODE)
                                    243 	.area GSINIT0 (CODE)
                                    244 	.area GSINIT1 (CODE)
                                    245 	.area GSINIT2 (CODE)
                                    246 	.area GSINIT3 (CODE)
                                    247 	.area GSINIT4 (CODE)
                                    248 	.area GSINIT5 (CODE)
                                    249 	.area GSINIT  (CODE)
                                    250 	.area GSFINAL (CODE)
                                    251 	.area CSEG    (CODE)
                                    252 ;--------------------------------------------------------
                                    253 ; global & static initialisations
                                    254 ;--------------------------------------------------------
                                    255 	.area HOME    (CODE)
                                    256 	.area GSINIT  (CODE)
                                    257 	.area GSFINAL (CODE)
                                    258 	.area GSINIT  (CODE)
                                    259 ;--------------------------------------------------------
                                    260 ; Home
                                    261 ;--------------------------------------------------------
                                    262 	.area HOME    (CODE)
                                    263 	.area HOME    (CODE)
                                    264 ;--------------------------------------------------------
                                    265 ; code
                                    266 ;--------------------------------------------------------
                                    267 	.area CSEG    (CODE)
                                    268 ;------------------------------------------------------------
                                    269 ;Allocation info for local variables in function 'enter_promiscuous_mode'
                                    270 ;------------------------------------------------------------
                                    271 ;sloc0                     Allocated with name '_enter_promiscuous_mode_sloc0_1_0'
                                    272 ;sloc1                     Allocated with name '_enter_promiscuous_mode_sloc1_1_0'
                                    273 ;prefix_length             Allocated with name '_enter_promiscuous_mode_PARM_2'
                                    274 ;prefix                    Allocated with name '_enter_promiscuous_mode_prefix_65536_38'
                                    275 ;x                         Allocated with name '_enter_promiscuous_mode_x_65536_39'
                                    276 ;address                   Allocated with name '_enter_promiscuous_mode_address_131072_41'
                                    277 ;------------------------------------------------------------
                                    278 ;	src/radio.c:9: void enter_promiscuous_mode(uint8_t * prefix, uint8_t prefix_length)
                                    279 ;	-----------------------------------------
                                    280 ;	 function enter_promiscuous_mode
                                    281 ;	-----------------------------------------
      0004C8                        282 _enter_promiscuous_mode:
                           000007   283 	ar7 = 0x07
                           000006   284 	ar6 = 0x06
                           000005   285 	ar5 = 0x05
                           000004   286 	ar4 = 0x04
                           000003   287 	ar3 = 0x03
                           000002   288 	ar2 = 0x02
                           000001   289 	ar1 = 0x01
                           000000   290 	ar0 = 0x00
      0004C8 AF F0            [24]  291 	mov	r7,b
      0004CA AE 83            [24]  292 	mov	r6,dph
      0004CC E5 82            [12]  293 	mov	a,dpl
      0004CE 90 80 1B         [24]  294 	mov	dptr,#_enter_promiscuous_mode_prefix_65536_38
      0004D1 F0               [24]  295 	movx	@dptr,a
      0004D2 EE               [12]  296 	mov	a,r6
      0004D3 A3               [24]  297 	inc	dptr
      0004D4 F0               [24]  298 	movx	@dptr,a
      0004D5 EF               [12]  299 	mov	a,r7
      0004D6 A3               [24]  300 	inc	dptr
      0004D7 F0               [24]  301 	movx	@dptr,a
                                    302 ;	src/radio.c:13: for(x = 0; x < prefix_length; x++) pm_prefix[prefix_length - 1 - x] = prefix[x];
      0004D8 90 80 1B         [24]  303 	mov	dptr,#_enter_promiscuous_mode_prefix_65536_38
      0004DB E0               [24]  304 	movx	a,@dptr
      0004DC F5 21            [12]  305 	mov	_enter_promiscuous_mode_sloc0_1_0,a
      0004DE A3               [24]  306 	inc	dptr
      0004DF E0               [24]  307 	movx	a,@dptr
      0004E0 F5 22            [12]  308 	mov	(_enter_promiscuous_mode_sloc0_1_0 + 1),a
      0004E2 A3               [24]  309 	inc	dptr
      0004E3 E0               [24]  310 	movx	a,@dptr
      0004E4 F5 23            [12]  311 	mov	(_enter_promiscuous_mode_sloc0_1_0 + 2),a
      0004E6 90 80 1A         [24]  312 	mov	dptr,#_enter_promiscuous_mode_PARM_2
      0004E9 E0               [24]  313 	movx	a,@dptr
      0004EA FC               [12]  314 	mov	r4,a
      0004EB 7A 00            [12]  315 	mov	r2,#0x00
      0004ED 7B 00            [12]  316 	mov	r3,#0x00
      0004EF                        317 00109$:
      0004EF 8C 00            [24]  318 	mov	ar0,r4
      0004F1 79 00            [12]  319 	mov	r1,#0x00
      0004F3 C3               [12]  320 	clr	c
      0004F4 EA               [12]  321 	mov	a,r2
      0004F5 98               [12]  322 	subb	a,r0
      0004F6 EB               [12]  323 	mov	a,r3
      0004F7 64 80            [12]  324 	xrl	a,#0x80
      0004F9 89 F0            [24]  325 	mov	b,r1
      0004FB 63 F0 80         [24]  326 	xrl	b,#0x80
      0004FE 95 F0            [12]  327 	subb	a,b
      000500 50 3C            [24]  328 	jnc	00101$
      000502 8C 07            [24]  329 	mov	ar7,r4
      000504 1F               [12]  330 	dec	r7
      000505 8A 06            [24]  331 	mov	ar6,r2
      000507 EF               [12]  332 	mov	a,r7
      000508 C3               [12]  333 	clr	c
      000509 9E               [12]  334 	subb	a,r6
      00050A FF               [12]  335 	mov	r7,a
      00050B 33               [12]  336 	rlc	a
      00050C 95 E0            [12]  337 	subb	a,acc
      00050E FE               [12]  338 	mov	r6,a
      00050F EF               [12]  339 	mov	a,r7
      000510 24 14            [12]  340 	add	a,#_pm_prefix
      000512 F5 24            [12]  341 	mov	_enter_promiscuous_mode_sloc1_1_0,a
      000514 EE               [12]  342 	mov	a,r6
      000515 34 80            [12]  343 	addc	a,#(_pm_prefix >> 8)
      000517 F5 25            [12]  344 	mov	(_enter_promiscuous_mode_sloc1_1_0 + 1),a
      000519 C0 04            [24]  345 	push	ar4
      00051B EA               [12]  346 	mov	a,r2
      00051C 25 21            [12]  347 	add	a,_enter_promiscuous_mode_sloc0_1_0
      00051E FC               [12]  348 	mov	r4,a
      00051F EB               [12]  349 	mov	a,r3
      000520 35 22            [12]  350 	addc	a,(_enter_promiscuous_mode_sloc0_1_0 + 1)
      000522 FD               [12]  351 	mov	r5,a
      000523 AF 23            [24]  352 	mov	r7,(_enter_promiscuous_mode_sloc0_1_0 + 2)
      000525 8C 82            [24]  353 	mov	dpl,r4
      000527 8D 83            [24]  354 	mov	dph,r5
      000529 8F F0            [24]  355 	mov	b,r7
      00052B 12 16 D1         [24]  356 	lcall	__gptrget
      00052E 85 24 82         [24]  357 	mov	dpl,_enter_promiscuous_mode_sloc1_1_0
      000531 85 25 83         [24]  358 	mov	dph,(_enter_promiscuous_mode_sloc1_1_0 + 1)
      000534 F0               [24]  359 	movx	@dptr,a
      000535 0A               [12]  360 	inc	r2
      000536 BA 00 01         [24]  361 	cjne	r2,#0x00,00143$
      000539 0B               [12]  362 	inc	r3
      00053A                        363 00143$:
      00053A D0 04            [24]  364 	pop	ar4
      00053C 80 B1            [24]  365 	sjmp	00109$
      00053E                        366 00101$:
                                    367 ;	src/radio.c:14: pm_prefix_length = prefix_length > 5 ? 5 : prefix_length;
      00053E EC               [12]  368 	mov	a,r4
      00053F 24 FA            [12]  369 	add	a,#0xff - 0x05
      000541 50 06            [24]  370 	jnc	00113$
      000543 7E 05            [12]  371 	mov	r6,#0x05
      000545 7F 00            [12]  372 	mov	r7,#0x00
      000547 80 04            [24]  373 	sjmp	00114$
      000549                        374 00113$:
      000549 88 06            [24]  375 	mov	ar6,r0
      00054B 89 07            [24]  376 	mov	ar7,r1
      00054D                        377 00114$:
      00054D 90 80 12         [24]  378 	mov	dptr,#_pm_prefix_length
      000550 EE               [12]  379 	mov	a,r6
      000551 F0               [24]  380 	movx	@dptr,a
      000552 EF               [12]  381 	mov	a,r7
      000553 A3               [24]  382 	inc	dptr
      000554 F0               [24]  383 	movx	@dptr,a
                                    384 ;	src/radio.c:15: radio_mode = promiscuous;
      000555 90 80 11         [24]  385 	mov	dptr,#_radio_mode
      000558 74 01            [12]  386 	mov	a,#0x01
      00055A F0               [24]  387 	movx	@dptr,a
                                    388 ;	src/radio.c:16: pm_payload_length = 32;
      00055B 90 80 19         [24]  389 	mov	dptr,#_pm_payload_length
      00055E 74 20            [12]  390 	mov	a,#0x20
      000560 F0               [24]  391 	movx	@dptr,a
                                    392 ;	src/radio.c:19: rfce = 0;
                                    393 ;	assignBit
      000561 C2 90            [12]  394 	clr	_rfce
                                    395 ;	src/radio.c:22: write_register_byte(EN_RXADDR, ENRX_P0);
      000563 90 80 3D         [24]  396 	mov	dptr,#_write_register_byte_PARM_2
      000566 74 01            [12]  397 	mov	a,#0x01
      000568 F0               [24]  398 	movx	@dptr,a
      000569 75 82 02         [24]  399 	mov	dpl,#0x02
      00056C 12 09 50         [24]  400 	lcall	_write_register_byte
                                    401 ;	src/radio.c:25: if(pm_prefix_length == 0) configure_address(promiscuous_address, 2);
      00056F 90 80 12         [24]  402 	mov	dptr,#_pm_prefix_length
      000572 E0               [24]  403 	movx	a,@dptr
      000573 FE               [12]  404 	mov	r6,a
      000574 A3               [24]  405 	inc	dptr
      000575 E0               [24]  406 	movx	a,@dptr
      000576 FF               [12]  407 	mov	r7,a
      000577 4E               [12]  408 	orl	a,r6
      000578 70 11            [24]  409 	jnz	00106$
      00057A 90 80 28         [24]  410 	mov	dptr,#_configure_address_PARM_2
      00057D 74 02            [12]  411 	mov	a,#0x02
      00057F F0               [24]  412 	movx	@dptr,a
      000580 90 80 C3         [24]  413 	mov	dptr,#_promiscuous_address
      000583 75 F0 00         [24]  414 	mov	b,#0x00
      000586 12 07 7E         [24]  415 	lcall	_configure_address
      000589 80 4C            [24]  416 	sjmp	00107$
      00058B                        417 00106$:
                                    418 ;	src/radio.c:28: else if(pm_prefix_length == 1)
      00058B BE 01 3B         [24]  419 	cjne	r6,#0x01,00103$
      00058E BF 00 38         [24]  420 	cjne	r7,#0x00,00103$
                                    421 ;	src/radio.c:30: uint8_t address[2] = { pm_prefix[0], (pm_prefix[0] & 0x80) == 0x80 ? 0xAA : 0x55 };
      000591 90 80 14         [24]  422 	mov	dptr,#_pm_prefix
      000594 E0               [24]  423 	movx	a,@dptr
      000595 90 80 1E         [24]  424 	mov	dptr,#_enter_promiscuous_mode_address_131072_41
      000598 F0               [24]  425 	movx	@dptr,a
      000599 90 80 14         [24]  426 	mov	dptr,#_pm_prefix
      00059C E0               [24]  427 	movx	a,@dptr
      00059D FD               [12]  428 	mov	r5,a
      00059E 53 05 80         [24]  429 	anl	ar5,#0x80
      0005A1 7C 00            [12]  430 	mov	r4,#0x00
      0005A3 BD 80 09         [24]  431 	cjne	r5,#0x80,00115$
      0005A6 BC 00 06         [24]  432 	cjne	r4,#0x00,00115$
      0005A9 7C AA            [12]  433 	mov	r4,#0xaa
      0005AB 7D 00            [12]  434 	mov	r5,#0x00
      0005AD 80 04            [24]  435 	sjmp	00116$
      0005AF                        436 00115$:
      0005AF 7C 55            [12]  437 	mov	r4,#0x55
      0005B1 7D 00            [12]  438 	mov	r5,#0x00
      0005B3                        439 00116$:
      0005B3 90 80 1F         [24]  440 	mov	dptr,#(_enter_promiscuous_mode_address_131072_41 + 0x0001)
      0005B6 EC               [12]  441 	mov	a,r4
      0005B7 F0               [24]  442 	movx	@dptr,a
                                    443 ;	src/radio.c:31: configure_address(address, 2);
      0005B8 90 80 28         [24]  444 	mov	dptr,#_configure_address_PARM_2
      0005BB 74 02            [12]  445 	mov	a,#0x02
      0005BD F0               [24]  446 	movx	@dptr,a
      0005BE 90 80 1E         [24]  447 	mov	dptr,#_enter_promiscuous_mode_address_131072_41
      0005C1 75 F0 00         [24]  448 	mov	b,#0x00
      0005C4 12 07 7E         [24]  449 	lcall	_configure_address
      0005C7 80 0E            [24]  450 	sjmp	00107$
      0005C9                        451 00103$:
                                    452 ;	src/radio.c:35: else configure_address(pm_prefix, pm_prefix_length);
      0005C9 90 80 28         [24]  453 	mov	dptr,#_configure_address_PARM_2
      0005CC EE               [12]  454 	mov	a,r6
      0005CD F0               [24]  455 	movx	@dptr,a
      0005CE 90 80 14         [24]  456 	mov	dptr,#_pm_prefix
      0005D1 75 F0 00         [24]  457 	mov	b,#0x00
      0005D4 12 07 7E         [24]  458 	lcall	_configure_address
      0005D7                        459 00107$:
                                    460 ;	src/radio.c:38: configure_mac(0, 0, ENAA_NONE);
      0005D7 90 80 2C         [24]  461 	mov	dptr,#_configure_mac_PARM_2
      0005DA E4               [12]  462 	clr	a
      0005DB F0               [24]  463 	movx	@dptr,a
      0005DC 90 80 2D         [24]  464 	mov	dptr,#_configure_mac_PARM_3
      0005DF F0               [24]  465 	movx	@dptr,a
      0005E0 75 82 00         [24]  466 	mov	dpl,#0x00
      0005E3 12 07 F7         [24]  467 	lcall	_configure_mac
                                    468 ;	src/radio.c:41: configure_phy(PRIM_RX | PWR_UP, RATE_2M, pm_payload_length);
      0005E6 90 80 19         [24]  469 	mov	dptr,#_pm_payload_length
      0005E9 E0               [24]  470 	movx	a,@dptr
      0005EA FF               [12]  471 	mov	r7,a
      0005EB 90 80 2F         [24]  472 	mov	dptr,#_configure_phy_PARM_2
      0005EE 74 08            [12]  473 	mov	a,#0x08
      0005F0 F0               [24]  474 	movx	@dptr,a
      0005F1 90 80 30         [24]  475 	mov	dptr,#_configure_phy_PARM_3
      0005F4 EF               [12]  476 	mov	a,r7
      0005F5 F0               [24]  477 	movx	@dptr,a
      0005F6 75 82 03         [24]  478 	mov	dpl,#0x03
      0005F9 12 08 24         [24]  479 	lcall	_configure_phy
                                    480 ;	src/radio.c:44: rfce = 1;
                                    481 ;	assignBit
      0005FC D2 90            [12]  482 	setb	_rfce
                                    483 ;	src/radio.c:45: in1bc = 0;
      0005FE 90 C7 B7         [24]  484 	mov	dptr,#0xc7b7
      000601 E4               [12]  485 	clr	a
      000602 F0               [24]  486 	movx	@dptr,a
                                    487 ;	src/radio.c:46: }
      000603 22               [24]  488 	ret
                                    489 ;------------------------------------------------------------
                                    490 ;Allocation info for local variables in function 'enter_promiscuous_mode_generic'
                                    491 ;------------------------------------------------------------
                                    492 ;sloc0                     Allocated with name '_enter_promiscuous_mode_generic_sloc0_1_0'
                                    493 ;sloc1                     Allocated with name '_enter_promiscuous_mode_generic_sloc1_1_0'
                                    494 ;prefix_length             Allocated with name '_enter_promiscuous_mode_generic_PARM_2'
                                    495 ;rate                      Allocated with name '_enter_promiscuous_mode_generic_PARM_3'
                                    496 ;payload_length            Allocated with name '_enter_promiscuous_mode_generic_PARM_4'
                                    497 ;prefix                    Allocated with name '_enter_promiscuous_mode_generic_prefix_65536_42'
                                    498 ;x                         Allocated with name '_enter_promiscuous_mode_generic_x_65536_43'
                                    499 ;address                   Allocated with name '_enter_promiscuous_mode_generic_address_131072_45'
                                    500 ;------------------------------------------------------------
                                    501 ;	src/radio.c:49: void enter_promiscuous_mode_generic(uint8_t * prefix, uint8_t prefix_length, uint8_t rate, uint8_t payload_length)
                                    502 ;	-----------------------------------------
                                    503 ;	 function enter_promiscuous_mode_generic
                                    504 ;	-----------------------------------------
      000604                        505 _enter_promiscuous_mode_generic:
      000604 AF F0            [24]  506 	mov	r7,b
      000606 AE 83            [24]  507 	mov	r6,dph
      000608 E5 82            [12]  508 	mov	a,dpl
      00060A 90 80 23         [24]  509 	mov	dptr,#_enter_promiscuous_mode_generic_prefix_65536_42
      00060D F0               [24]  510 	movx	@dptr,a
      00060E EE               [12]  511 	mov	a,r6
      00060F A3               [24]  512 	inc	dptr
      000610 F0               [24]  513 	movx	@dptr,a
      000611 EF               [12]  514 	mov	a,r7
      000612 A3               [24]  515 	inc	dptr
      000613 F0               [24]  516 	movx	@dptr,a
                                    517 ;	src/radio.c:53: for(x = 0; x < prefix_length; x++) pm_prefix[prefix_length - 1 - x] = prefix[x];
      000614 90 80 23         [24]  518 	mov	dptr,#_enter_promiscuous_mode_generic_prefix_65536_42
      000617 E0               [24]  519 	movx	a,@dptr
      000618 F5 26            [12]  520 	mov	_enter_promiscuous_mode_generic_sloc0_1_0,a
      00061A A3               [24]  521 	inc	dptr
      00061B E0               [24]  522 	movx	a,@dptr
      00061C F5 27            [12]  523 	mov	(_enter_promiscuous_mode_generic_sloc0_1_0 + 1),a
      00061E A3               [24]  524 	inc	dptr
      00061F E0               [24]  525 	movx	a,@dptr
      000620 F5 28            [12]  526 	mov	(_enter_promiscuous_mode_generic_sloc0_1_0 + 2),a
      000622 90 80 20         [24]  527 	mov	dptr,#_enter_promiscuous_mode_generic_PARM_2
      000625 E0               [24]  528 	movx	a,@dptr
      000626 FC               [12]  529 	mov	r4,a
      000627 7A 00            [12]  530 	mov	r2,#0x00
      000629 7B 00            [12]  531 	mov	r3,#0x00
      00062B                        532 00113$:
      00062B 8C 00            [24]  533 	mov	ar0,r4
      00062D 79 00            [12]  534 	mov	r1,#0x00
      00062F C3               [12]  535 	clr	c
      000630 EA               [12]  536 	mov	a,r2
      000631 98               [12]  537 	subb	a,r0
      000632 EB               [12]  538 	mov	a,r3
      000633 64 80            [12]  539 	xrl	a,#0x80
      000635 89 F0            [24]  540 	mov	b,r1
      000637 63 F0 80         [24]  541 	xrl	b,#0x80
      00063A 95 F0            [12]  542 	subb	a,b
      00063C 50 3C            [24]  543 	jnc	00101$
      00063E 8C 07            [24]  544 	mov	ar7,r4
      000640 1F               [12]  545 	dec	r7
      000641 8A 06            [24]  546 	mov	ar6,r2
      000643 EF               [12]  547 	mov	a,r7
      000644 C3               [12]  548 	clr	c
      000645 9E               [12]  549 	subb	a,r6
      000646 FF               [12]  550 	mov	r7,a
      000647 33               [12]  551 	rlc	a
      000648 95 E0            [12]  552 	subb	a,acc
      00064A FE               [12]  553 	mov	r6,a
      00064B EF               [12]  554 	mov	a,r7
      00064C 24 14            [12]  555 	add	a,#_pm_prefix
      00064E F5 29            [12]  556 	mov	_enter_promiscuous_mode_generic_sloc1_1_0,a
      000650 EE               [12]  557 	mov	a,r6
      000651 34 80            [12]  558 	addc	a,#(_pm_prefix >> 8)
      000653 F5 2A            [12]  559 	mov	(_enter_promiscuous_mode_generic_sloc1_1_0 + 1),a
      000655 C0 04            [24]  560 	push	ar4
      000657 EA               [12]  561 	mov	a,r2
      000658 25 26            [12]  562 	add	a,_enter_promiscuous_mode_generic_sloc0_1_0
      00065A FC               [12]  563 	mov	r4,a
      00065B EB               [12]  564 	mov	a,r3
      00065C 35 27            [12]  565 	addc	a,(_enter_promiscuous_mode_generic_sloc0_1_0 + 1)
      00065E FD               [12]  566 	mov	r5,a
      00065F AF 28            [24]  567 	mov	r7,(_enter_promiscuous_mode_generic_sloc0_1_0 + 2)
      000661 8C 82            [24]  568 	mov	dpl,r4
      000663 8D 83            [24]  569 	mov	dph,r5
      000665 8F F0            [24]  570 	mov	b,r7
      000667 12 16 D1         [24]  571 	lcall	__gptrget
      00066A 85 29 82         [24]  572 	mov	dpl,_enter_promiscuous_mode_generic_sloc1_1_0
      00066D 85 2A 83         [24]  573 	mov	dph,(_enter_promiscuous_mode_generic_sloc1_1_0 + 1)
      000670 F0               [24]  574 	movx	@dptr,a
      000671 0A               [12]  575 	inc	r2
      000672 BA 00 01         [24]  576 	cjne	r2,#0x00,00155$
      000675 0B               [12]  577 	inc	r3
      000676                        578 00155$:
      000676 D0 04            [24]  579 	pop	ar4
      000678 80 B1            [24]  580 	sjmp	00113$
      00067A                        581 00101$:
                                    582 ;	src/radio.c:54: pm_prefix_length = prefix_length > 5 ? 5 : prefix_length;
      00067A EC               [12]  583 	mov	a,r4
      00067B 24 FA            [12]  584 	add	a,#0xff - 0x05
      00067D 50 06            [24]  585 	jnc	00117$
      00067F 7E 05            [12]  586 	mov	r6,#0x05
      000681 7F 00            [12]  587 	mov	r7,#0x00
      000683 80 04            [24]  588 	sjmp	00118$
      000685                        589 00117$:
      000685 88 06            [24]  590 	mov	ar6,r0
      000687 89 07            [24]  591 	mov	ar7,r1
      000689                        592 00118$:
      000689 90 80 12         [24]  593 	mov	dptr,#_pm_prefix_length
      00068C EE               [12]  594 	mov	a,r6
      00068D F0               [24]  595 	movx	@dptr,a
      00068E EF               [12]  596 	mov	a,r7
      00068F A3               [24]  597 	inc	dptr
      000690 F0               [24]  598 	movx	@dptr,a
                                    599 ;	src/radio.c:55: radio_mode = promiscuous_generic;
      000691 90 80 11         [24]  600 	mov	dptr,#_radio_mode
      000694 74 02            [12]  601 	mov	a,#0x02
      000696 F0               [24]  602 	movx	@dptr,a
                                    603 ;	src/radio.c:56: pm_payload_length = payload_length;
      000697 90 80 22         [24]  604 	mov	dptr,#_enter_promiscuous_mode_generic_PARM_4
      00069A E0               [24]  605 	movx	a,@dptr
      00069B 90 80 19         [24]  606 	mov	dptr,#_pm_payload_length
      00069E F0               [24]  607 	movx	@dptr,a
                                    608 ;	src/radio.c:59: rfce = 0;
                                    609 ;	assignBit
      00069F C2 90            [12]  610 	clr	_rfce
                                    611 ;	src/radio.c:62: write_register_byte(EN_RXADDR, ENRX_P0);
      0006A1 90 80 3D         [24]  612 	mov	dptr,#_write_register_byte_PARM_2
      0006A4 74 01            [12]  613 	mov	a,#0x01
      0006A6 F0               [24]  614 	movx	@dptr,a
      0006A7 75 82 02         [24]  615 	mov	dpl,#0x02
      0006AA 12 09 50         [24]  616 	lcall	_write_register_byte
                                    617 ;	src/radio.c:65: if(pm_prefix_length == 0) configure_address(promiscuous_address, 2);
      0006AD 90 80 12         [24]  618 	mov	dptr,#_pm_prefix_length
      0006B0 E0               [24]  619 	movx	a,@dptr
      0006B1 FE               [12]  620 	mov	r6,a
      0006B2 A3               [24]  621 	inc	dptr
      0006B3 E0               [24]  622 	movx	a,@dptr
      0006B4 FF               [12]  623 	mov	r7,a
      0006B5 4E               [12]  624 	orl	a,r6
      0006B6 70 11            [24]  625 	jnz	00106$
      0006B8 90 80 28         [24]  626 	mov	dptr,#_configure_address_PARM_2
      0006BB 74 02            [12]  627 	mov	a,#0x02
      0006BD F0               [24]  628 	movx	@dptr,a
      0006BE 90 80 C3         [24]  629 	mov	dptr,#_promiscuous_address
      0006C1 75 F0 00         [24]  630 	mov	b,#0x00
      0006C4 12 07 7E         [24]  631 	lcall	_configure_address
      0006C7 80 4C            [24]  632 	sjmp	00107$
      0006C9                        633 00106$:
                                    634 ;	src/radio.c:68: else if(pm_prefix_length == 1)
      0006C9 BE 01 3B         [24]  635 	cjne	r6,#0x01,00103$
      0006CC BF 00 38         [24]  636 	cjne	r7,#0x00,00103$
                                    637 ;	src/radio.c:70: uint8_t address[2] = { pm_prefix[0], (pm_prefix[0] & 0x80) == 0x80 ? 0xAA : 0x55 };
      0006CF 90 80 14         [24]  638 	mov	dptr,#_pm_prefix
      0006D2 E0               [24]  639 	movx	a,@dptr
      0006D3 90 80 26         [24]  640 	mov	dptr,#_enter_promiscuous_mode_generic_address_131072_45
      0006D6 F0               [24]  641 	movx	@dptr,a
      0006D7 90 80 14         [24]  642 	mov	dptr,#_pm_prefix
      0006DA E0               [24]  643 	movx	a,@dptr
      0006DB FD               [12]  644 	mov	r5,a
      0006DC 53 05 80         [24]  645 	anl	ar5,#0x80
      0006DF 7C 00            [12]  646 	mov	r4,#0x00
      0006E1 BD 80 09         [24]  647 	cjne	r5,#0x80,00119$
      0006E4 BC 00 06         [24]  648 	cjne	r4,#0x00,00119$
      0006E7 7C AA            [12]  649 	mov	r4,#0xaa
      0006E9 7D 00            [12]  650 	mov	r5,#0x00
      0006EB 80 04            [24]  651 	sjmp	00120$
      0006ED                        652 00119$:
      0006ED 7C 55            [12]  653 	mov	r4,#0x55
      0006EF 7D 00            [12]  654 	mov	r5,#0x00
      0006F1                        655 00120$:
      0006F1 90 80 27         [24]  656 	mov	dptr,#(_enter_promiscuous_mode_generic_address_131072_45 + 0x0001)
      0006F4 EC               [12]  657 	mov	a,r4
      0006F5 F0               [24]  658 	movx	@dptr,a
                                    659 ;	src/radio.c:71: configure_address(address, 2);
      0006F6 90 80 28         [24]  660 	mov	dptr,#_configure_address_PARM_2
      0006F9 74 02            [12]  661 	mov	a,#0x02
      0006FB F0               [24]  662 	movx	@dptr,a
      0006FC 90 80 26         [24]  663 	mov	dptr,#_enter_promiscuous_mode_generic_address_131072_45
      0006FF 75 F0 00         [24]  664 	mov	b,#0x00
      000702 12 07 7E         [24]  665 	lcall	_configure_address
      000705 80 0E            [24]  666 	sjmp	00107$
      000707                        667 00103$:
                                    668 ;	src/radio.c:75: else configure_address(pm_prefix, pm_prefix_length);
      000707 90 80 28         [24]  669 	mov	dptr,#_configure_address_PARM_2
      00070A EE               [12]  670 	mov	a,r6
      00070B F0               [24]  671 	movx	@dptr,a
      00070C 90 80 14         [24]  672 	mov	dptr,#_pm_prefix
      00070F 75 F0 00         [24]  673 	mov	b,#0x00
      000712 12 07 7E         [24]  674 	lcall	_configure_address
      000715                        675 00107$:
                                    676 ;	src/radio.c:78: configure_mac(0, 0, ENAA_NONE);
      000715 90 80 2C         [24]  677 	mov	dptr,#_configure_mac_PARM_2
      000718 E4               [12]  678 	clr	a
      000719 F0               [24]  679 	movx	@dptr,a
      00071A 90 80 2D         [24]  680 	mov	dptr,#_configure_mac_PARM_3
      00071D F0               [24]  681 	movx	@dptr,a
      00071E 75 82 00         [24]  682 	mov	dpl,#0x00
      000721 12 07 F7         [24]  683 	lcall	_configure_mac
                                    684 ;	src/radio.c:81: switch(rate)
      000724 90 80 21         [24]  685 	mov	dptr,#_enter_promiscuous_mode_generic_PARM_3
      000727 E0               [24]  686 	movx	a,@dptr
      000728 FF               [12]  687 	mov	r7,a
      000729 60 05            [24]  688 	jz	00108$
                                    689 ;	src/radio.c:83: case 0:  configure_phy(PRIM_RX | PWR_UP, RF_PWR_4 | RATE_250K, pm_payload_length); break;
      00072B BF 01 32         [24]  690 	cjne	r7,#0x01,00110$
      00072E 80 18            [24]  691 	sjmp	00109$
      000730                        692 00108$:
      000730 90 80 19         [24]  693 	mov	dptr,#_pm_payload_length
      000733 E0               [24]  694 	movx	a,@dptr
      000734 FF               [12]  695 	mov	r7,a
      000735 90 80 2F         [24]  696 	mov	dptr,#_configure_phy_PARM_2
      000738 74 26            [12]  697 	mov	a,#0x26
      00073A F0               [24]  698 	movx	@dptr,a
      00073B 90 80 30         [24]  699 	mov	dptr,#_configure_phy_PARM_3
      00073E EF               [12]  700 	mov	a,r7
      00073F F0               [24]  701 	movx	@dptr,a
      000740 75 82 03         [24]  702 	mov	dpl,#0x03
      000743 12 08 24         [24]  703 	lcall	_configure_phy
                                    704 ;	src/radio.c:84: case 1:  configure_phy(PRIM_RX | PWR_UP, RF_PWR_4 | RATE_1M, pm_payload_length); break;
      000746 80 2E            [24]  705 	sjmp	00111$
      000748                        706 00109$:
      000748 90 80 19         [24]  707 	mov	dptr,#_pm_payload_length
      00074B E0               [24]  708 	movx	a,@dptr
      00074C FF               [12]  709 	mov	r7,a
      00074D 90 80 2F         [24]  710 	mov	dptr,#_configure_phy_PARM_2
      000750 74 06            [12]  711 	mov	a,#0x06
      000752 F0               [24]  712 	movx	@dptr,a
      000753 90 80 30         [24]  713 	mov	dptr,#_configure_phy_PARM_3
      000756 EF               [12]  714 	mov	a,r7
      000757 F0               [24]  715 	movx	@dptr,a
      000758 75 82 03         [24]  716 	mov	dpl,#0x03
      00075B 12 08 24         [24]  717 	lcall	_configure_phy
                                    718 ;	src/radio.c:85: default: configure_phy(PRIM_RX | PWR_UP, RF_PWR_4 | RATE_2M, pm_payload_length); break;
      00075E 80 16            [24]  719 	sjmp	00111$
      000760                        720 00110$:
      000760 90 80 19         [24]  721 	mov	dptr,#_pm_payload_length
      000763 E0               [24]  722 	movx	a,@dptr
      000764 FF               [12]  723 	mov	r7,a
      000765 90 80 2F         [24]  724 	mov	dptr,#_configure_phy_PARM_2
      000768 74 0E            [12]  725 	mov	a,#0x0e
      00076A F0               [24]  726 	movx	@dptr,a
      00076B 90 80 30         [24]  727 	mov	dptr,#_configure_phy_PARM_3
      00076E EF               [12]  728 	mov	a,r7
      00076F F0               [24]  729 	movx	@dptr,a
      000770 75 82 03         [24]  730 	mov	dpl,#0x03
      000773 12 08 24         [24]  731 	lcall	_configure_phy
                                    732 ;	src/radio.c:86: }
      000776                        733 00111$:
                                    734 ;	src/radio.c:89: rfce = 1;
                                    735 ;	assignBit
      000776 D2 90            [12]  736 	setb	_rfce
                                    737 ;	src/radio.c:90: in1bc = 0;
      000778 90 C7 B7         [24]  738 	mov	dptr,#0xc7b7
      00077B E4               [12]  739 	clr	a
      00077C F0               [24]  740 	movx	@dptr,a
                                    741 ;	src/radio.c:91: }
      00077D 22               [24]  742 	ret
                                    743 ;------------------------------------------------------------
                                    744 ;Allocation info for local variables in function 'configure_address'
                                    745 ;------------------------------------------------------------
                                    746 ;length                    Allocated with name '_configure_address_PARM_2'
                                    747 ;address                   Allocated with name '_configure_address_address_65536_47'
                                    748 ;------------------------------------------------------------
                                    749 ;	src/radio.c:94: void configure_address(uint8_t * address, uint8_t length)
                                    750 ;	-----------------------------------------
                                    751 ;	 function configure_address
                                    752 ;	-----------------------------------------
      00077E                        753 _configure_address:
      00077E AF F0            [24]  754 	mov	r7,b
      000780 AE 83            [24]  755 	mov	r6,dph
      000782 E5 82            [12]  756 	mov	a,dpl
      000784 90 80 29         [24]  757 	mov	dptr,#_configure_address_address_65536_47
      000787 F0               [24]  758 	movx	@dptr,a
      000788 EE               [12]  759 	mov	a,r6
      000789 A3               [24]  760 	inc	dptr
      00078A F0               [24]  761 	movx	@dptr,a
      00078B EF               [12]  762 	mov	a,r7
      00078C A3               [24]  763 	inc	dptr
      00078D F0               [24]  764 	movx	@dptr,a
                                    765 ;	src/radio.c:96: write_register_byte(EN_RXADDR, ENRX_P0);
      00078E 90 80 3D         [24]  766 	mov	dptr,#_write_register_byte_PARM_2
      000791 74 01            [12]  767 	mov	a,#0x01
      000793 F0               [24]  768 	movx	@dptr,a
      000794 75 82 02         [24]  769 	mov	dpl,#0x02
      000797 12 09 50         [24]  770 	lcall	_write_register_byte
                                    771 ;	src/radio.c:97: write_register_byte(SETUP_AW, length - 2);
      00079A 90 80 28         [24]  772 	mov	dptr,#_configure_address_PARM_2
      00079D E0               [24]  773 	movx	a,@dptr
      00079E FF               [12]  774 	mov	r7,a
      00079F FE               [12]  775 	mov	r6,a
      0007A0 1E               [12]  776 	dec	r6
      0007A1 1E               [12]  777 	dec	r6
      0007A2 90 80 3D         [24]  778 	mov	dptr,#_write_register_byte_PARM_2
      0007A5 EE               [12]  779 	mov	a,r6
      0007A6 F0               [24]  780 	movx	@dptr,a
      0007A7 75 82 03         [24]  781 	mov	dpl,#0x03
      0007AA C0 07            [24]  782 	push	ar7
      0007AC 12 09 50         [24]  783 	lcall	_write_register_byte
      0007AF D0 07            [24]  784 	pop	ar7
                                    785 ;	src/radio.c:98: write_register(TX_ADDR, address, length);
      0007B1 90 80 29         [24]  786 	mov	dptr,#_configure_address_address_65536_47
      0007B4 E0               [24]  787 	movx	a,@dptr
      0007B5 FC               [12]  788 	mov	r4,a
      0007B6 A3               [24]  789 	inc	dptr
      0007B7 E0               [24]  790 	movx	a,@dptr
      0007B8 FD               [12]  791 	mov	r5,a
      0007B9 A3               [24]  792 	inc	dptr
      0007BA E0               [24]  793 	movx	a,@dptr
      0007BB FE               [12]  794 	mov	r6,a
      0007BC 90 80 33         [24]  795 	mov	dptr,#_spi_write_PARM_2
      0007BF EC               [12]  796 	mov	a,r4
      0007C0 F0               [24]  797 	movx	@dptr,a
      0007C1 ED               [12]  798 	mov	a,r5
      0007C2 A3               [24]  799 	inc	dptr
      0007C3 F0               [24]  800 	movx	@dptr,a
      0007C4 EE               [12]  801 	mov	a,r6
      0007C5 A3               [24]  802 	inc	dptr
      0007C6 F0               [24]  803 	movx	@dptr,a
      0007C7 90 80 36         [24]  804 	mov	dptr,#_spi_write_PARM_3
      0007CA EF               [12]  805 	mov	a,r7
      0007CB F0               [24]  806 	movx	@dptr,a
      0007CC 75 82 30         [24]  807 	mov	dpl,#0x30
      0007CF C0 07            [24]  808 	push	ar7
      0007D1 12 08 63         [24]  809 	lcall	_spi_write
      0007D4 D0 07            [24]  810 	pop	ar7
                                    811 ;	src/radio.c:99: write_register(RX_ADDR_P0, address, length);
      0007D6 90 80 29         [24]  812 	mov	dptr,#_configure_address_address_65536_47
      0007D9 E0               [24]  813 	movx	a,@dptr
      0007DA FC               [12]  814 	mov	r4,a
      0007DB A3               [24]  815 	inc	dptr
      0007DC E0               [24]  816 	movx	a,@dptr
      0007DD FD               [12]  817 	mov	r5,a
      0007DE A3               [24]  818 	inc	dptr
      0007DF E0               [24]  819 	movx	a,@dptr
      0007E0 FE               [12]  820 	mov	r6,a
      0007E1 90 80 33         [24]  821 	mov	dptr,#_spi_write_PARM_2
      0007E4 EC               [12]  822 	mov	a,r4
      0007E5 F0               [24]  823 	movx	@dptr,a
      0007E6 ED               [12]  824 	mov	a,r5
      0007E7 A3               [24]  825 	inc	dptr
      0007E8 F0               [24]  826 	movx	@dptr,a
      0007E9 EE               [12]  827 	mov	a,r6
      0007EA A3               [24]  828 	inc	dptr
      0007EB F0               [24]  829 	movx	@dptr,a
      0007EC 90 80 36         [24]  830 	mov	dptr,#_spi_write_PARM_3
      0007EF EF               [12]  831 	mov	a,r7
      0007F0 F0               [24]  832 	movx	@dptr,a
      0007F1 75 82 2A         [24]  833 	mov	dpl,#0x2a
                                    834 ;	src/radio.c:100: }
      0007F4 02 08 63         [24]  835 	ljmp	_spi_write
                                    836 ;------------------------------------------------------------
                                    837 ;Allocation info for local variables in function 'configure_mac'
                                    838 ;------------------------------------------------------------
                                    839 ;dynpd                     Allocated with name '_configure_mac_PARM_2'
                                    840 ;en_aa                     Allocated with name '_configure_mac_PARM_3'
                                    841 ;feature                   Allocated with name '_configure_mac_feature_65536_49'
                                    842 ;------------------------------------------------------------
                                    843 ;	src/radio.c:103: void configure_mac(uint8_t feature, uint8_t dynpd, uint8_t en_aa)
                                    844 ;	-----------------------------------------
                                    845 ;	 function configure_mac
                                    846 ;	-----------------------------------------
      0007F7                        847 _configure_mac:
      0007F7 E5 82            [12]  848 	mov	a,dpl
      0007F9 90 80 2E         [24]  849 	mov	dptr,#_configure_mac_feature_65536_49
      0007FC F0               [24]  850 	movx	@dptr,a
                                    851 ;	src/radio.c:105: write_register_byte(FEATURE, feature);
      0007FD E0               [24]  852 	movx	a,@dptr
      0007FE 90 80 3D         [24]  853 	mov	dptr,#_write_register_byte_PARM_2
      000801 F0               [24]  854 	movx	@dptr,a
      000802 75 82 1D         [24]  855 	mov	dpl,#0x1d
      000805 12 09 50         [24]  856 	lcall	_write_register_byte
                                    857 ;	src/radio.c:106: write_register_byte(DYNPD, dynpd);
      000808 90 80 2C         [24]  858 	mov	dptr,#_configure_mac_PARM_2
      00080B E0               [24]  859 	movx	a,@dptr
      00080C 90 80 3D         [24]  860 	mov	dptr,#_write_register_byte_PARM_2
      00080F F0               [24]  861 	movx	@dptr,a
      000810 75 82 1C         [24]  862 	mov	dpl,#0x1c
      000813 12 09 50         [24]  863 	lcall	_write_register_byte
                                    864 ;	src/radio.c:107: write_register_byte(EN_AA, en_aa);
      000816 90 80 2D         [24]  865 	mov	dptr,#_configure_mac_PARM_3
      000819 E0               [24]  866 	movx	a,@dptr
      00081A 90 80 3D         [24]  867 	mov	dptr,#_write_register_byte_PARM_2
      00081D F0               [24]  868 	movx	@dptr,a
      00081E 75 82 01         [24]  869 	mov	dpl,#0x01
                                    870 ;	src/radio.c:108: }
      000821 02 09 50         [24]  871 	ljmp	_write_register_byte
                                    872 ;------------------------------------------------------------
                                    873 ;Allocation info for local variables in function 'configure_phy'
                                    874 ;------------------------------------------------------------
                                    875 ;rf_setup                  Allocated with name '_configure_phy_PARM_2'
                                    876 ;rx_pw                     Allocated with name '_configure_phy_PARM_3'
                                    877 ;config                    Allocated with name '_configure_phy_config_65536_51'
                                    878 ;------------------------------------------------------------
                                    879 ;	src/radio.c:111: void configure_phy(uint8_t config, uint8_t rf_setup, uint8_t rx_pw)
                                    880 ;	-----------------------------------------
                                    881 ;	 function configure_phy
                                    882 ;	-----------------------------------------
      000824                        883 _configure_phy:
      000824 E5 82            [12]  884 	mov	a,dpl
      000826 90 80 31         [24]  885 	mov	dptr,#_configure_phy_config_65536_51
      000829 F0               [24]  886 	movx	@dptr,a
                                    887 ;	src/radio.c:113: write_register_byte(CONFIG, config);
      00082A E0               [24]  888 	movx	a,@dptr
      00082B 90 80 3D         [24]  889 	mov	dptr,#_write_register_byte_PARM_2
      00082E F0               [24]  890 	movx	@dptr,a
      00082F 75 82 00         [24]  891 	mov	dpl,#0x00
      000832 12 09 50         [24]  892 	lcall	_write_register_byte
                                    893 ;	src/radio.c:114: write_register_byte(RF_SETUP, rf_setup);
      000835 90 80 2F         [24]  894 	mov	dptr,#_configure_phy_PARM_2
      000838 E0               [24]  895 	movx	a,@dptr
      000839 90 80 3D         [24]  896 	mov	dptr,#_write_register_byte_PARM_2
      00083C F0               [24]  897 	movx	@dptr,a
      00083D 75 82 06         [24]  898 	mov	dpl,#0x06
      000840 12 09 50         [24]  899 	lcall	_write_register_byte
                                    900 ;	src/radio.c:115: write_register_byte(RX_PW_P0, rx_pw);
      000843 90 80 30         [24]  901 	mov	dptr,#_configure_phy_PARM_3
      000846 E0               [24]  902 	movx	a,@dptr
      000847 90 80 3D         [24]  903 	mov	dptr,#_write_register_byte_PARM_2
      00084A F0               [24]  904 	movx	@dptr,a
      00084B 75 82 11         [24]  905 	mov	dpl,#0x11
                                    906 ;	src/radio.c:116: }
      00084E 02 09 50         [24]  907 	ljmp	_write_register_byte
                                    908 ;------------------------------------------------------------
                                    909 ;Allocation info for local variables in function 'spi_transfer'
                                    910 ;------------------------------------------------------------
                                    911 ;byte                      Allocated with name '_spi_transfer_byte_65536_53'
                                    912 ;------------------------------------------------------------
                                    913 ;	src/radio.c:119: uint8_t spi_transfer(uint8_t byte)
                                    914 ;	-----------------------------------------
                                    915 ;	 function spi_transfer
                                    916 ;	-----------------------------------------
      000851                        917 _spi_transfer:
      000851 E5 82            [12]  918 	mov	a,dpl
      000853 90 80 32         [24]  919 	mov	dptr,#_spi_transfer_byte_65536_53
      000856 F0               [24]  920 	movx	@dptr,a
                                    921 ;	src/radio.c:121: RFDAT = byte;
      000857 E0               [24]  922 	movx	a,@dptr
      000858 F5 E5            [12]  923 	mov	_RFDAT,a
                                    924 ;	src/radio.c:122: RFRDY = 0;
                                    925 ;	assignBit
      00085A C2 C0            [12]  926 	clr	_RFRDY
                                    927 ;	src/radio.c:123: while(!RFRDY);
      00085C                        928 00101$:
      00085C 30 C0 FD         [24]  929 	jnb	_RFRDY,00101$
                                    930 ;	src/radio.c:124: return RFDAT;
      00085F 85 E5 82         [24]  931 	mov	dpl,_RFDAT
                                    932 ;	src/radio.c:125: }
      000862 22               [24]  933 	ret
                                    934 ;------------------------------------------------------------
                                    935 ;Allocation info for local variables in function 'spi_write'
                                    936 ;------------------------------------------------------------
                                    937 ;buffer                    Allocated with name '_spi_write_PARM_2'
                                    938 ;length                    Allocated with name '_spi_write_PARM_3'
                                    939 ;command                   Allocated with name '_spi_write_command_65536_55'
                                    940 ;x                         Allocated with name '_spi_write_x_65536_56'
                                    941 ;------------------------------------------------------------
                                    942 ;	src/radio.c:128: void spi_write(uint8_t command, uint8_t * buffer, uint8_t length)
                                    943 ;	-----------------------------------------
                                    944 ;	 function spi_write
                                    945 ;	-----------------------------------------
      000863                        946 _spi_write:
      000863 E5 82            [12]  947 	mov	a,dpl
      000865 90 80 37         [24]  948 	mov	dptr,#_spi_write_command_65536_55
      000868 F0               [24]  949 	movx	@dptr,a
                                    950 ;	src/radio.c:131: rfcsn = 0;
                                    951 ;	assignBit
      000869 C2 91            [12]  952 	clr	_rfcsn
                                    953 ;	src/radio.c:132: spi_transfer(command);
      00086B 90 80 37         [24]  954 	mov	dptr,#_spi_write_command_65536_55
      00086E E0               [24]  955 	movx	a,@dptr
      00086F F5 82            [12]  956 	mov	dpl,a
      000871 12 08 51         [24]  957 	lcall	_spi_transfer
                                    958 ;	src/radio.c:133: for(x = 0; x < length; x++) spi_transfer(buffer[x]);
      000874 90 80 33         [24]  959 	mov	dptr,#_spi_write_PARM_2
      000877 E0               [24]  960 	movx	a,@dptr
      000878 FD               [12]  961 	mov	r5,a
      000879 A3               [24]  962 	inc	dptr
      00087A E0               [24]  963 	movx	a,@dptr
      00087B FE               [12]  964 	mov	r6,a
      00087C A3               [24]  965 	inc	dptr
      00087D E0               [24]  966 	movx	a,@dptr
      00087E FF               [12]  967 	mov	r7,a
      00087F 90 80 36         [24]  968 	mov	dptr,#_spi_write_PARM_3
      000882 E0               [24]  969 	movx	a,@dptr
      000883 FC               [12]  970 	mov	r4,a
      000884 7A 00            [12]  971 	mov	r2,#0x00
      000886 7B 00            [12]  972 	mov	r3,#0x00
      000888                        973 00103$:
      000888 8C 00            [24]  974 	mov	ar0,r4
      00088A 79 00            [12]  975 	mov	r1,#0x00
      00088C C3               [12]  976 	clr	c
      00088D EA               [12]  977 	mov	a,r2
      00088E 98               [12]  978 	subb	a,r0
      00088F EB               [12]  979 	mov	a,r3
      000890 64 80            [12]  980 	xrl	a,#0x80
      000892 89 F0            [24]  981 	mov	b,r1
      000894 63 F0 80         [24]  982 	xrl	b,#0x80
      000897 95 F0            [12]  983 	subb	a,b
      000899 50 39            [24]  984 	jnc	00101$
      00089B C0 04            [24]  985 	push	ar4
      00089D EA               [12]  986 	mov	a,r2
      00089E 2D               [12]  987 	add	a,r5
      00089F F8               [12]  988 	mov	r0,a
      0008A0 EB               [12]  989 	mov	a,r3
      0008A1 3E               [12]  990 	addc	a,r6
      0008A2 F9               [12]  991 	mov	r1,a
      0008A3 8F 04            [24]  992 	mov	ar4,r7
      0008A5 88 82            [24]  993 	mov	dpl,r0
      0008A7 89 83            [24]  994 	mov	dph,r1
      0008A9 8C F0            [24]  995 	mov	b,r4
      0008AB 12 16 D1         [24]  996 	lcall	__gptrget
      0008AE F5 82            [12]  997 	mov	dpl,a
      0008B0 C0 07            [24]  998 	push	ar7
      0008B2 C0 06            [24]  999 	push	ar6
      0008B4 C0 05            [24] 1000 	push	ar5
      0008B6 C0 04            [24] 1001 	push	ar4
      0008B8 C0 03            [24] 1002 	push	ar3
      0008BA C0 02            [24] 1003 	push	ar2
      0008BC 12 08 51         [24] 1004 	lcall	_spi_transfer
      0008BF D0 02            [24] 1005 	pop	ar2
      0008C1 D0 03            [24] 1006 	pop	ar3
      0008C3 D0 04            [24] 1007 	pop	ar4
      0008C5 D0 05            [24] 1008 	pop	ar5
      0008C7 D0 06            [24] 1009 	pop	ar6
      0008C9 D0 07            [24] 1010 	pop	ar7
      0008CB 0A               [12] 1011 	inc	r2
      0008CC BA 00 01         [24] 1012 	cjne	r2,#0x00,00117$
      0008CF 0B               [12] 1013 	inc	r3
      0008D0                       1014 00117$:
      0008D0 D0 04            [24] 1015 	pop	ar4
      0008D2 80 B4            [24] 1016 	sjmp	00103$
      0008D4                       1017 00101$:
                                   1018 ;	src/radio.c:134: rfcsn = 1;
                                   1019 ;	assignBit
      0008D4 D2 91            [12] 1020 	setb	_rfcsn
                                   1021 ;	src/radio.c:135: }
      0008D6 22               [24] 1022 	ret
                                   1023 ;------------------------------------------------------------
                                   1024 ;Allocation info for local variables in function 'spi_read'
                                   1025 ;------------------------------------------------------------
                                   1026 ;sloc0                     Allocated with name '_spi_read_sloc0_1_0'
                                   1027 ;buffer                    Allocated with name '_spi_read_PARM_2'
                                   1028 ;length                    Allocated with name '_spi_read_PARM_3'
                                   1029 ;command                   Allocated with name '_spi_read_command_65536_58'
                                   1030 ;x                         Allocated with name '_spi_read_x_65536_59'
                                   1031 ;------------------------------------------------------------
                                   1032 ;	src/radio.c:138: void spi_read(uint8_t command, uint8_t * buffer, uint8_t length)
                                   1033 ;	-----------------------------------------
                                   1034 ;	 function spi_read
                                   1035 ;	-----------------------------------------
      0008D7                       1036 _spi_read:
      0008D7 E5 82            [12] 1037 	mov	a,dpl
      0008D9 90 80 3C         [24] 1038 	mov	dptr,#_spi_read_command_65536_58
      0008DC F0               [24] 1039 	movx	@dptr,a
                                   1040 ;	src/radio.c:141: rfcsn = 0;
                                   1041 ;	assignBit
      0008DD C2 91            [12] 1042 	clr	_rfcsn
                                   1043 ;	src/radio.c:142: spi_transfer(command);
      0008DF 90 80 3C         [24] 1044 	mov	dptr,#_spi_read_command_65536_58
      0008E2 E0               [24] 1045 	movx	a,@dptr
      0008E3 F5 82            [12] 1046 	mov	dpl,a
      0008E5 12 08 51         [24] 1047 	lcall	_spi_transfer
                                   1048 ;	src/radio.c:143: for(x = 0; x < length; x++) buffer[x] = spi_transfer(0xFF);
      0008E8 90 80 38         [24] 1049 	mov	dptr,#_spi_read_PARM_2
      0008EB E0               [24] 1050 	movx	a,@dptr
      0008EC FD               [12] 1051 	mov	r5,a
      0008ED A3               [24] 1052 	inc	dptr
      0008EE E0               [24] 1053 	movx	a,@dptr
      0008EF FE               [12] 1054 	mov	r6,a
      0008F0 A3               [24] 1055 	inc	dptr
      0008F1 E0               [24] 1056 	movx	a,@dptr
      0008F2 FF               [12] 1057 	mov	r7,a
      0008F3 90 80 3B         [24] 1058 	mov	dptr,#_spi_read_PARM_3
      0008F6 E0               [24] 1059 	movx	a,@dptr
      0008F7 FC               [12] 1060 	mov	r4,a
      0008F8 7A 00            [12] 1061 	mov	r2,#0x00
      0008FA 7B 00            [12] 1062 	mov	r3,#0x00
      0008FC                       1063 00103$:
      0008FC 8C 00            [24] 1064 	mov	ar0,r4
      0008FE 79 00            [12] 1065 	mov	r1,#0x00
      000900 C3               [12] 1066 	clr	c
      000901 EA               [12] 1067 	mov	a,r2
      000902 98               [12] 1068 	subb	a,r0
      000903 EB               [12] 1069 	mov	a,r3
      000904 64 80            [12] 1070 	xrl	a,#0x80
      000906 89 F0            [24] 1071 	mov	b,r1
      000908 63 F0 80         [24] 1072 	xrl	b,#0x80
      00090B 95 F0            [12] 1073 	subb	a,b
      00090D 50 3E            [24] 1074 	jnc	00101$
      00090F C0 04            [24] 1075 	push	ar4
      000911 EA               [12] 1076 	mov	a,r2
      000912 2D               [12] 1077 	add	a,r5
      000913 F5 2B            [12] 1078 	mov	_spi_read_sloc0_1_0,a
      000915 EB               [12] 1079 	mov	a,r3
      000916 3E               [12] 1080 	addc	a,r6
      000917 F5 2C            [12] 1081 	mov	(_spi_read_sloc0_1_0 + 1),a
      000919 8F 2D            [24] 1082 	mov	(_spi_read_sloc0_1_0 + 2),r7
      00091B 75 82 FF         [24] 1083 	mov	dpl,#0xff
      00091E C0 07            [24] 1084 	push	ar7
      000920 C0 06            [24] 1085 	push	ar6
      000922 C0 05            [24] 1086 	push	ar5
      000924 C0 03            [24] 1087 	push	ar3
      000926 C0 02            [24] 1088 	push	ar2
      000928 12 08 51         [24] 1089 	lcall	_spi_transfer
      00092B AC 82            [24] 1090 	mov	r4,dpl
      00092D D0 02            [24] 1091 	pop	ar2
      00092F D0 03            [24] 1092 	pop	ar3
      000931 D0 05            [24] 1093 	pop	ar5
      000933 D0 06            [24] 1094 	pop	ar6
      000935 D0 07            [24] 1095 	pop	ar7
      000937 85 2B 82         [24] 1096 	mov	dpl,_spi_read_sloc0_1_0
      00093A 85 2C 83         [24] 1097 	mov	dph,(_spi_read_sloc0_1_0 + 1)
      00093D 85 2D F0         [24] 1098 	mov	b,(_spi_read_sloc0_1_0 + 2)
      000940 EC               [12] 1099 	mov	a,r4
      000941 12 16 9E         [24] 1100 	lcall	__gptrput
      000944 0A               [12] 1101 	inc	r2
      000945 BA 00 01         [24] 1102 	cjne	r2,#0x00,00117$
      000948 0B               [12] 1103 	inc	r3
      000949                       1104 00117$:
      000949 D0 04            [24] 1105 	pop	ar4
      00094B 80 AF            [24] 1106 	sjmp	00103$
      00094D                       1107 00101$:
                                   1108 ;	src/radio.c:144: rfcsn = 1;
                                   1109 ;	assignBit
      00094D D2 91            [12] 1110 	setb	_rfcsn
                                   1111 ;	src/radio.c:145: }
      00094F 22               [24] 1112 	ret
                                   1113 ;------------------------------------------------------------
                                   1114 ;Allocation info for local variables in function 'write_register_byte'
                                   1115 ;------------------------------------------------------------
                                   1116 ;byte                      Allocated with name '_write_register_byte_PARM_2'
                                   1117 ;reg                       Allocated with name '_write_register_byte_reg_65536_61'
                                   1118 ;------------------------------------------------------------
                                   1119 ;	src/radio.c:148: void write_register_byte(uint8_t reg, uint8_t byte)
                                   1120 ;	-----------------------------------------
                                   1121 ;	 function write_register_byte
                                   1122 ;	-----------------------------------------
      000950                       1123 _write_register_byte:
      000950 E5 82            [12] 1124 	mov	a,dpl
      000952 90 80 3E         [24] 1125 	mov	dptr,#_write_register_byte_reg_65536_61
      000955 F0               [24] 1126 	movx	@dptr,a
                                   1127 ;	src/radio.c:150: write_register(reg, &byte, 1);
      000956 E0               [24] 1128 	movx	a,@dptr
      000957 44 20            [12] 1129 	orl	a,#0x20
      000959 FF               [12] 1130 	mov	r7,a
      00095A 90 80 33         [24] 1131 	mov	dptr,#_spi_write_PARM_2
      00095D 74 3D            [12] 1132 	mov	a,#_write_register_byte_PARM_2
      00095F F0               [24] 1133 	movx	@dptr,a
      000960 74 80            [12] 1134 	mov	a,#(_write_register_byte_PARM_2 >> 8)
      000962 A3               [24] 1135 	inc	dptr
      000963 F0               [24] 1136 	movx	@dptr,a
      000964 E4               [12] 1137 	clr	a
      000965 A3               [24] 1138 	inc	dptr
      000966 F0               [24] 1139 	movx	@dptr,a
      000967 90 80 36         [24] 1140 	mov	dptr,#_spi_write_PARM_3
      00096A 04               [12] 1141 	inc	a
      00096B F0               [24] 1142 	movx	@dptr,a
      00096C 8F 82            [24] 1143 	mov	dpl,r7
                                   1144 ;	src/radio.c:151: }
      00096E 02 08 63         [24] 1145 	ljmp	_spi_write
                                   1146 ;------------------------------------------------------------
                                   1147 ;Allocation info for local variables in function 'read_register_byte'
                                   1148 ;------------------------------------------------------------
                                   1149 ;reg                       Allocated with name '_read_register_byte_reg_65536_63'
                                   1150 ;value                     Allocated with name '_read_register_byte_value_65536_64'
                                   1151 ;------------------------------------------------------------
                                   1152 ;	src/radio.c:154: uint8_t read_register_byte(uint8_t reg)
                                   1153 ;	-----------------------------------------
                                   1154 ;	 function read_register_byte
                                   1155 ;	-----------------------------------------
      000971                       1156 _read_register_byte:
      000971 E5 82            [12] 1157 	mov	a,dpl
      000973 90 80 3F         [24] 1158 	mov	dptr,#_read_register_byte_reg_65536_63
      000976 F0               [24] 1159 	movx	@dptr,a
                                   1160 ;	src/radio.c:157: read_register(reg, &value, 1);
      000977 E0               [24] 1161 	movx	a,@dptr
      000978 FF               [12] 1162 	mov	r7,a
      000979 90 80 38         [24] 1163 	mov	dptr,#_spi_read_PARM_2
      00097C 74 40            [12] 1164 	mov	a,#_read_register_byte_value_65536_64
      00097E F0               [24] 1165 	movx	@dptr,a
      00097F 74 80            [12] 1166 	mov	a,#(_read_register_byte_value_65536_64 >> 8)
      000981 A3               [24] 1167 	inc	dptr
      000982 F0               [24] 1168 	movx	@dptr,a
      000983 E4               [12] 1169 	clr	a
      000984 A3               [24] 1170 	inc	dptr
      000985 F0               [24] 1171 	movx	@dptr,a
      000986 90 80 3B         [24] 1172 	mov	dptr,#_spi_read_PARM_3
      000989 04               [12] 1173 	inc	a
      00098A F0               [24] 1174 	movx	@dptr,a
      00098B 8F 82            [24] 1175 	mov	dpl,r7
      00098D 12 08 D7         [24] 1176 	lcall	_spi_read
                                   1177 ;	src/radio.c:158: return value;
      000990 90 80 40         [24] 1178 	mov	dptr,#_read_register_byte_value_65536_64
      000993 E0               [24] 1179 	movx	a,@dptr
                                   1180 ;	src/radio.c:159: }
      000994 F5 82            [12] 1181 	mov	dpl,a
      000996 22               [24] 1182 	ret
                                   1183 ;------------------------------------------------------------
                                   1184 ;Allocation info for local variables in function 'crc_update'
                                   1185 ;------------------------------------------------------------
                                   1186 ;byte                      Allocated with name '_crc_update_PARM_2'
                                   1187 ;bits                      Allocated with name '_crc_update_PARM_3'
                                   1188 ;crc                       Allocated with name '_crc_update_crc_65536_65'
                                   1189 ;------------------------------------------------------------
                                   1190 ;	src/radio.c:162: uint16_t crc_update(uint16_t crc, uint8_t byte, uint8_t bits)
                                   1191 ;	-----------------------------------------
                                   1192 ;	 function crc_update
                                   1193 ;	-----------------------------------------
      000997                       1194 _crc_update:
      000997 AF 83            [24] 1195 	mov	r7,dph
      000999 E5 82            [12] 1196 	mov	a,dpl
      00099B 90 80 43         [24] 1197 	mov	dptr,#_crc_update_crc_65536_65
      00099E F0               [24] 1198 	movx	@dptr,a
      00099F EF               [12] 1199 	mov	a,r7
      0009A0 A3               [24] 1200 	inc	dptr
      0009A1 F0               [24] 1201 	movx	@dptr,a
                                   1202 ;	src/radio.c:164: crc = crc ^ (byte << 8);
      0009A2 90 80 41         [24] 1203 	mov	dptr,#_crc_update_PARM_2
      0009A5 E0               [24] 1204 	movx	a,@dptr
      0009A6 FE               [12] 1205 	mov	r6,a
      0009A7 7F 00            [12] 1206 	mov	r7,#0x00
      0009A9 90 80 43         [24] 1207 	mov	dptr,#_crc_update_crc_65536_65
      0009AC E0               [24] 1208 	movx	a,@dptr
      0009AD FC               [12] 1209 	mov	r4,a
      0009AE A3               [24] 1210 	inc	dptr
      0009AF E0               [24] 1211 	movx	a,@dptr
      0009B0 FD               [12] 1212 	mov	r5,a
      0009B1 EF               [12] 1213 	mov	a,r7
      0009B2 62 04            [12] 1214 	xrl	ar4,a
      0009B4 EE               [12] 1215 	mov	a,r6
      0009B5 62 05            [12] 1216 	xrl	ar5,a
      0009B7 90 80 43         [24] 1217 	mov	dptr,#_crc_update_crc_65536_65
      0009BA EC               [12] 1218 	mov	a,r4
      0009BB F0               [24] 1219 	movx	@dptr,a
      0009BC ED               [12] 1220 	mov	a,r5
      0009BD A3               [24] 1221 	inc	dptr
      0009BE F0               [24] 1222 	movx	@dptr,a
                                   1223 ;	src/radio.c:165: while(bits--)
      0009BF 90 80 42         [24] 1224 	mov	dptr,#_crc_update_PARM_3
      0009C2 E0               [24] 1225 	movx	a,@dptr
      0009C3 FF               [12] 1226 	mov	r7,a
      0009C4                       1227 00104$:
      0009C4 8F 06            [24] 1228 	mov	ar6,r7
      0009C6 1F               [12] 1229 	dec	r7
      0009C7 EE               [12] 1230 	mov	a,r6
      0009C8 60 3D            [24] 1231 	jz	00106$
                                   1232 ;	src/radio.c:166: if((crc & 0x8000) == 0x8000) crc = (crc << 1) ^ 0x1021;
      0009CA 90 80 43         [24] 1233 	mov	dptr,#_crc_update_crc_65536_65
      0009CD E0               [24] 1234 	movx	a,@dptr
      0009CE FD               [12] 1235 	mov	r5,a
      0009CF A3               [24] 1236 	inc	dptr
      0009D0 E0               [24] 1237 	movx	a,@dptr
      0009D1 FE               [12] 1238 	mov	r6,a
      0009D2 8D 03            [24] 1239 	mov	ar3,r5
      0009D4 8E 04            [24] 1240 	mov	ar4,r6
      0009D6 7B 00            [12] 1241 	mov	r3,#0x00
      0009D8 53 04 80         [24] 1242 	anl	ar4,#0x80
      0009DB BB 00 19         [24] 1243 	cjne	r3,#0x00,00102$
      0009DE BC 80 16         [24] 1244 	cjne	r4,#0x80,00102$
      0009E1 ED               [12] 1245 	mov	a,r5
      0009E2 2D               [12] 1246 	add	a,r5
      0009E3 FB               [12] 1247 	mov	r3,a
      0009E4 EE               [12] 1248 	mov	a,r6
      0009E5 33               [12] 1249 	rlc	a
      0009E6 FC               [12] 1250 	mov	r4,a
      0009E7 63 03 21         [24] 1251 	xrl	ar3,#0x21
      0009EA 63 04 10         [24] 1252 	xrl	ar4,#0x10
      0009ED 90 80 43         [24] 1253 	mov	dptr,#_crc_update_crc_65536_65
      0009F0 EB               [12] 1254 	mov	a,r3
      0009F1 F0               [24] 1255 	movx	@dptr,a
      0009F2 EC               [12] 1256 	mov	a,r4
      0009F3 A3               [24] 1257 	inc	dptr
      0009F4 F0               [24] 1258 	movx	@dptr,a
      0009F5 80 CD            [24] 1259 	sjmp	00104$
      0009F7                       1260 00102$:
                                   1261 ;	src/radio.c:167: else crc = crc << 1;
      0009F7 ED               [12] 1262 	mov	a,r5
      0009F8 2D               [12] 1263 	add	a,r5
      0009F9 FD               [12] 1264 	mov	r5,a
      0009FA EE               [12] 1265 	mov	a,r6
      0009FB 33               [12] 1266 	rlc	a
      0009FC FE               [12] 1267 	mov	r6,a
      0009FD 90 80 43         [24] 1268 	mov	dptr,#_crc_update_crc_65536_65
      000A00 ED               [12] 1269 	mov	a,r5
      000A01 F0               [24] 1270 	movx	@dptr,a
      000A02 EE               [12] 1271 	mov	a,r6
      000A03 A3               [24] 1272 	inc	dptr
      000A04 F0               [24] 1273 	movx	@dptr,a
      000A05 80 BD            [24] 1274 	sjmp	00104$
      000A07                       1275 00106$:
                                   1276 ;	src/radio.c:168: crc = crc & 0xFFFF;
      000A07 90 80 43         [24] 1277 	mov	dptr,#_crc_update_crc_65536_65
      000A0A E0               [24] 1278 	movx	a,@dptr
      000A0B FE               [12] 1279 	mov	r6,a
      000A0C A3               [24] 1280 	inc	dptr
      000A0D E0               [24] 1281 	movx	a,@dptr
      000A0E FF               [12] 1282 	mov	r7,a
      000A0F 90 80 43         [24] 1283 	mov	dptr,#_crc_update_crc_65536_65
      000A12 EE               [12] 1284 	mov	a,r6
      000A13 F0               [24] 1285 	movx	@dptr,a
      000A14 EF               [12] 1286 	mov	a,r7
      000A15 A3               [24] 1287 	inc	dptr
      000A16 F0               [24] 1288 	movx	@dptr,a
                                   1289 ;	src/radio.c:169: return crc;
      000A17 90 80 43         [24] 1290 	mov	dptr,#_crc_update_crc_65536_65
      000A1A E0               [24] 1291 	movx	a,@dptr
      000A1B FE               [12] 1292 	mov	r6,a
      000A1C A3               [24] 1293 	inc	dptr
      000A1D E0               [24] 1294 	movx	a,@dptr
                                   1295 ;	src/radio.c:170: }
      000A1E 8E 82            [24] 1296 	mov	dpl,r6
      000A20 F5 83            [12] 1297 	mov	dph,a
      000A22 22               [24] 1298 	ret
                                   1299 ;------------------------------------------------------------
                                   1300 ;Allocation info for local variables in function 'handle_radio_request'
                                   1301 ;------------------------------------------------------------
                                   1302 ;sloc0                     Allocated with name '_handle_radio_request_sloc0_1_0'
                                   1303 ;sloc1                     Allocated with name '_handle_radio_request_sloc1_1_0'
                                   1304 ;sloc2                     Allocated with name '_handle_radio_request_sloc2_1_0'
                                   1305 ;data                      Allocated with name '_handle_radio_request_PARM_2'
                                   1306 ;request                   Allocated with name '_handle_radio_request_request_65536_67'
                                   1307 ;command                   Allocated with name '_handle_radio_request_command_131072_70'
                                   1308 ;command_length            Allocated with name '_handle_radio_request_command_length_131072_70'
                                   1309 ;x                         Allocated with name '_handle_radio_request_x_131072_70'
                                   1310 ;value                     Allocated with name '_handle_radio_request_value_131072_79'
                                   1311 ;x                         Allocated with name '_handle_radio_request_x_262144_84'
                                   1312 ;offset                    Allocated with name '_handle_radio_request_offset_262144_84'
                                   1313 ;payload_length            Allocated with name '_handle_radio_request_payload_length_262144_84'
                                   1314 ;crc                       Allocated with name '_handle_radio_request_crc_262144_84'
                                   1315 ;crc_given                 Allocated with name '_handle_radio_request_crc_given_262144_84'
                                   1316 ;payload                   Allocated with name '_handle_radio_request_payload_262144_84'
                                   1317 ;x                         Allocated with name '_handle_radio_request_x_262144_95'
                                   1318 ;payload                   Allocated with name '_handle_radio_request_payload_262144_95'
                                   1319 ;elapsed                   Allocated with name '_handle_radio_request_elapsed_131072_98'
                                   1320 ;status                    Allocated with name '_handle_radio_request_status_131072_98'
                                   1321 ;__2621440005              Allocated with name '_handle_radio_request___2621440005_262144_108'
                                   1322 ;us                        Allocated with name '_handle_radio_request_us_327680_109'
                                   1323 ;__1966080007              Allocated with name '_handle_radio_request___1966080007_196608_111'
                                   1324 ;us                        Allocated with name '_handle_radio_request_us_262144_112'
                                   1325 ;address_start             Allocated with name '_handle_radio_request_address_start_131072_105'
                                   1326 ;__1966080009              Allocated with name '_handle_radio_request___1966080009_196608_114'
                                   1327 ;us                        Allocated with name '_handle_radio_request_us_262144_115'
                                   1328 ;------------------------------------------------------------
                                   1329 ;	src/radio.c:173: void handle_radio_request(uint8_t request, uint8_t * data)
                                   1330 ;	-----------------------------------------
                                   1331 ;	 function handle_radio_request
                                   1332 ;	-----------------------------------------
      000A23                       1333 _handle_radio_request:
      000A23 E5 82            [12] 1334 	mov	a,dpl
      000A25 90 80 48         [24] 1335 	mov	dptr,#_handle_radio_request_request_65536_67
      000A28 F0               [24] 1336 	movx	@dptr,a
                                   1337 ;	src/radio.c:176: if(request == LAUNCH_NORDIC_BOOTLOADER)
      000A29 E0               [24] 1338 	movx	a,@dptr
      000A2A FF               [12] 1339 	mov	r7,a
      000A2B BF FF 0E         [24] 1340 	cjne	r7,#0xff,00102$
                                   1341 ;	src/radio.c:178: nordic_bootloader();
      000A2E 90 80 BF         [24] 1342 	mov	dptr,#_nordic_bootloader
      000A31 E0               [24] 1343 	movx	a,@dptr
      000A32 F8               [12] 1344 	mov	r0,a
      000A33 A3               [24] 1345 	inc	dptr
      000A34 E0               [24] 1346 	movx	a,@dptr
      000A35 F5 83            [12] 1347 	mov	dph,a
      000A37 88 82            [24] 1348 	mov	dpl,r0
                                   1349 ;	src/radio.c:179: return;
      000A39 02 00 69         [24] 1350 	ljmp	__sdcc_call_dptr
      000A3C                       1351 00102$:
                                   1352 ;	src/radio.c:183: if(request == LAUNCH_LOGITECH_BOOTLOADER)
      000A3C BF FE 69         [24] 1353 	cjne	r7,#0xfe,00210$
                                   1354 ;	src/radio.c:185: const uint8_t command[9] = {'E', 'n', 't', 'e', 'r', ' ', 'I', 'C', 'P'};
      000A3F 90 80 49         [24] 1355 	mov	dptr,#_handle_radio_request_command_131072_70
      000A42 74 45            [12] 1356 	mov	a,#0x45
      000A44 F0               [24] 1357 	movx	@dptr,a
      000A45 90 80 4A         [24] 1358 	mov	dptr,#(_handle_radio_request_command_131072_70 + 0x0001)
      000A48 74 6E            [12] 1359 	mov	a,#0x6e
      000A4A F0               [24] 1360 	movx	@dptr,a
      000A4B 90 80 4B         [24] 1361 	mov	dptr,#(_handle_radio_request_command_131072_70 + 0x0002)
      000A4E 74 74            [12] 1362 	mov	a,#0x74
      000A50 F0               [24] 1363 	movx	@dptr,a
      000A51 90 80 4C         [24] 1364 	mov	dptr,#(_handle_radio_request_command_131072_70 + 0x0003)
      000A54 74 65            [12] 1365 	mov	a,#0x65
      000A56 F0               [24] 1366 	movx	@dptr,a
      000A57 90 80 4D         [24] 1367 	mov	dptr,#(_handle_radio_request_command_131072_70 + 0x0004)
      000A5A 74 72            [12] 1368 	mov	a,#0x72
      000A5C F0               [24] 1369 	movx	@dptr,a
      000A5D 90 80 4E         [24] 1370 	mov	dptr,#(_handle_radio_request_command_131072_70 + 0x0005)
      000A60 74 20            [12] 1371 	mov	a,#0x20
      000A62 F0               [24] 1372 	movx	@dptr,a
      000A63 90 80 4F         [24] 1373 	mov	dptr,#(_handle_radio_request_command_131072_70 + 0x0006)
      000A66 74 49            [12] 1374 	mov	a,#0x49
      000A68 F0               [24] 1375 	movx	@dptr,a
      000A69 90 80 50         [24] 1376 	mov	dptr,#(_handle_radio_request_command_131072_70 + 0x0007)
      000A6C 74 43            [12] 1377 	mov	a,#0x43
      000A6E F0               [24] 1378 	movx	@dptr,a
      000A6F 90 80 51         [24] 1379 	mov	dptr,#(_handle_radio_request_command_131072_70 + 0x0008)
      000A72 74 50            [12] 1380 	mov	a,#0x50
      000A74 F0               [24] 1381 	movx	@dptr,a
                                   1382 ;	src/radio.c:188: for(x = 0; x < command_length; x++)
      000A75 7D 00            [12] 1383 	mov	r5,#0x00
      000A77 7E 00            [12] 1384 	mov	r6,#0x00
      000A79                       1385 00225$:
      000A79 C3               [12] 1386 	clr	c
      000A7A ED               [12] 1387 	mov	a,r5
      000A7B 94 09            [12] 1388 	subb	a,#0x09
      000A7D EE               [12] 1389 	mov	a,r6
      000A7E 64 80            [12] 1390 	xrl	a,#0x80
      000A80 94 80            [12] 1391 	subb	a,#0x80
      000A82 50 16            [24] 1392 	jnc	00103$
                                   1393 ;	src/radio.c:190: AESIA1 = x;
                                   1394 ;	src/radio.c:191: AESIV = command[x];
      000A84 ED               [12] 1395 	mov	a,r5
      000A85 F5 F5            [12] 1396 	mov	_AESIA1,a
      000A87 24 49            [12] 1397 	add	a,#_handle_radio_request_command_131072_70
      000A89 F5 82            [12] 1398 	mov	dpl,a
      000A8B EE               [12] 1399 	mov	a,r6
      000A8C 34 80            [12] 1400 	addc	a,#(_handle_radio_request_command_131072_70 >> 8)
      000A8E F5 83            [12] 1401 	mov	dph,a
      000A90 E0               [24] 1402 	movx	a,@dptr
      000A91 F5 F2            [12] 1403 	mov	_AESIV,a
                                   1404 ;	src/radio.c:188: for(x = 0; x < command_length; x++)
      000A93 0D               [12] 1405 	inc	r5
      000A94 BD 00 E2         [24] 1406 	cjne	r5,#0x00,00225$
      000A97 0E               [12] 1407 	inc	r6
      000A98 80 DF            [24] 1408 	sjmp	00225$
      000A9A                       1409 00103$:
                                   1410 ;	src/radio.c:193: logitech_bootloader();
      000A9A 90 80 C1         [24] 1411 	mov	dptr,#_logitech_bootloader
      000A9D E0               [24] 1412 	movx	a,@dptr
      000A9E F8               [12] 1413 	mov	r0,a
      000A9F A3               [24] 1414 	inc	dptr
      000AA0 E0               [24] 1415 	movx	a,@dptr
      000AA1 F5 83            [12] 1416 	mov	dph,a
      000AA3 88 82            [24] 1417 	mov	dpl,r0
                                   1418 ;	src/radio.c:194: return;
      000AA5 02 00 69         [24] 1419 	ljmp	__sdcc_call_dptr
      000AA8                       1420 00210$:
                                   1421 ;	src/radio.c:198: else if(request == ENABLE_LNA)
      000AA8 BF 0B 0C         [24] 1422 	cjne	r7,#0x0b,00207$
                                   1423 ;	src/radio.c:200: P0DIR &= ~0x10;
      000AAB 53 94 EF         [24] 1424 	anl	_P0DIR,#0xef
                                   1425 ;	src/radio.c:201: P0 |= 0x10;
      000AAE 43 80 10         [24] 1426 	orl	_P0,#0x10
                                   1427 ;	src/radio.c:202: in1bc = 0;
      000AB1 90 C7 B7         [24] 1428 	mov	dptr,#0xc7b7
      000AB4 E4               [12] 1429 	clr	a
      000AB5 F0               [24] 1430 	movx	@dptr,a
                                   1431 ;	src/radio.c:203: return;
      000AB6 22               [24] 1432 	ret
      000AB7                       1433 00207$:
                                   1434 ;	src/radio.c:207: else if(request == SET_CHANNEL)
      000AB7 BF 09 68         [24] 1435 	cjne	r7,#0x09,00204$
                                   1436 ;	src/radio.c:209: rfce = 0;
                                   1437 ;	assignBit
      000ABA C2 90            [12] 1438 	clr	_rfce
                                   1439 ;	src/radio.c:210: write_register_byte(RF_CH, data[0]);
      000ABC 90 80 45         [24] 1440 	mov	dptr,#_handle_radio_request_PARM_2
      000ABF E0               [24] 1441 	movx	a,@dptr
      000AC0 FC               [12] 1442 	mov	r4,a
      000AC1 A3               [24] 1443 	inc	dptr
      000AC2 E0               [24] 1444 	movx	a,@dptr
      000AC3 FD               [12] 1445 	mov	r5,a
      000AC4 A3               [24] 1446 	inc	dptr
      000AC5 E0               [24] 1447 	movx	a,@dptr
      000AC6 FE               [12] 1448 	mov	r6,a
      000AC7 8C 82            [24] 1449 	mov	dpl,r4
      000AC9 8D 83            [24] 1450 	mov	dph,r5
      000ACB 8E F0            [24] 1451 	mov	b,r6
      000ACD 12 16 D1         [24] 1452 	lcall	__gptrget
      000AD0 90 80 3D         [24] 1453 	mov	dptr,#_write_register_byte_PARM_2
      000AD3 F0               [24] 1454 	movx	@dptr,a
      000AD4 75 82 05         [24] 1455 	mov	dpl,#0x05
      000AD7 C0 06            [24] 1456 	push	ar6
      000AD9 C0 05            [24] 1457 	push	ar5
      000ADB C0 04            [24] 1458 	push	ar4
      000ADD 12 09 50         [24] 1459 	lcall	_write_register_byte
      000AE0 D0 04            [24] 1460 	pop	ar4
      000AE2 D0 05            [24] 1461 	pop	ar5
      000AE4 D0 06            [24] 1462 	pop	ar6
                                   1463 ;	src/radio.c:211: in1bc = 1;
      000AE6 90 C7 B7         [24] 1464 	mov	dptr,#0xc7b7
      000AE9 74 01            [12] 1465 	mov	a,#0x01
      000AEB F0               [24] 1466 	movx	@dptr,a
                                   1467 ;	src/radio.c:212: in1buf[0] = data[0];
      000AEC 8C 82            [24] 1468 	mov	dpl,r4
      000AEE 8D 83            [24] 1469 	mov	dph,r5
      000AF0 8E F0            [24] 1470 	mov	b,r6
      000AF2 12 16 D1         [24] 1471 	lcall	__gptrget
      000AF5 90 C6 80         [24] 1472 	mov	dptr,#_in1buf
      000AF8 F0               [24] 1473 	movx	@dptr,a
                                   1474 ;	src/radio.c:213: flush_rx();
      000AF9 90 80 33         [24] 1475 	mov	dptr,#_spi_write_PARM_2
      000AFC E4               [12] 1476 	clr	a
      000AFD F0               [24] 1477 	movx	@dptr,a
      000AFE A3               [24] 1478 	inc	dptr
      000AFF F0               [24] 1479 	movx	@dptr,a
      000B00 A3               [24] 1480 	inc	dptr
      000B01 F0               [24] 1481 	movx	@dptr,a
      000B02 90 80 36         [24] 1482 	mov	dptr,#_spi_write_PARM_3
      000B05 F0               [24] 1483 	movx	@dptr,a
      000B06 75 82 E2         [24] 1484 	mov	dpl,#0xe2
      000B09 12 08 63         [24] 1485 	lcall	_spi_write
                                   1486 ;	src/radio.c:214: flush_tx();
      000B0C 90 80 33         [24] 1487 	mov	dptr,#_spi_write_PARM_2
      000B0F E4               [12] 1488 	clr	a
      000B10 F0               [24] 1489 	movx	@dptr,a
      000B11 A3               [24] 1490 	inc	dptr
      000B12 F0               [24] 1491 	movx	@dptr,a
      000B13 A3               [24] 1492 	inc	dptr
      000B14 F0               [24] 1493 	movx	@dptr,a
      000B15 90 80 36         [24] 1494 	mov	dptr,#_spi_write_PARM_3
      000B18 F0               [24] 1495 	movx	@dptr,a
      000B19 75 82 E1         [24] 1496 	mov	dpl,#0xe1
      000B1C 12 08 63         [24] 1497 	lcall	_spi_write
                                   1498 ;	src/radio.c:215: rfce = 1;
                                   1499 ;	assignBit
      000B1F D2 90            [12] 1500 	setb	_rfce
                                   1501 ;	src/radio.c:216: return;
      000B21 22               [24] 1502 	ret
      000B22                       1503 00204$:
                                   1504 ;	src/radio.c:220: else if(request == GET_CHANNEL)
      000B22 BF 0A 1F         [24] 1505 	cjne	r7,#0x0a,00201$
                                   1506 ;	src/radio.c:222: spi_read(RF_CH, in1buf, 1);
      000B25 90 80 38         [24] 1507 	mov	dptr,#_spi_read_PARM_2
      000B28 74 80            [12] 1508 	mov	a,#_in1buf
      000B2A F0               [24] 1509 	movx	@dptr,a
      000B2B 74 C6            [12] 1510 	mov	a,#(_in1buf >> 8)
      000B2D A3               [24] 1511 	inc	dptr
      000B2E F0               [24] 1512 	movx	@dptr,a
      000B2F E4               [12] 1513 	clr	a
      000B30 A3               [24] 1514 	inc	dptr
      000B31 F0               [24] 1515 	movx	@dptr,a
      000B32 90 80 3B         [24] 1516 	mov	dptr,#_spi_read_PARM_3
      000B35 04               [12] 1517 	inc	a
      000B36 F0               [24] 1518 	movx	@dptr,a
      000B37 75 82 05         [24] 1519 	mov	dpl,#0x05
      000B3A 12 08 D7         [24] 1520 	lcall	_spi_read
                                   1521 ;	src/radio.c:223: in1bc = 1;
      000B3D 90 C7 B7         [24] 1522 	mov	dptr,#0xc7b7
      000B40 74 01            [12] 1523 	mov	a,#0x01
      000B42 F0               [24] 1524 	movx	@dptr,a
                                   1525 ;	src/radio.c:224: return;
      000B43 22               [24] 1526 	ret
      000B44                       1527 00201$:
                                   1528 ;	src/radio.c:228: else if(request == ENTER_PROMISCUOUS_MODE)
      000B44 BF 06 2A         [24] 1529 	cjne	r7,#0x06,00198$
                                   1530 ;	src/radio.c:230: enter_promiscuous_mode(&data[1] /* address prefix */, data[0] /* prefix length */);
      000B47 90 80 45         [24] 1531 	mov	dptr,#_handle_radio_request_PARM_2
      000B4A E0               [24] 1532 	movx	a,@dptr
      000B4B FC               [12] 1533 	mov	r4,a
      000B4C A3               [24] 1534 	inc	dptr
      000B4D E0               [24] 1535 	movx	a,@dptr
      000B4E FD               [12] 1536 	mov	r5,a
      000B4F A3               [24] 1537 	inc	dptr
      000B50 E0               [24] 1538 	movx	a,@dptr
      000B51 FE               [12] 1539 	mov	r6,a
      000B52 74 01            [12] 1540 	mov	a,#0x01
      000B54 2C               [12] 1541 	add	a,r4
      000B55 F9               [12] 1542 	mov	r1,a
      000B56 E4               [12] 1543 	clr	a
      000B57 3D               [12] 1544 	addc	a,r5
      000B58 FA               [12] 1545 	mov	r2,a
      000B59 8E 03            [24] 1546 	mov	ar3,r6
      000B5B 8C 82            [24] 1547 	mov	dpl,r4
      000B5D 8D 83            [24] 1548 	mov	dph,r5
      000B5F 8E F0            [24] 1549 	mov	b,r6
      000B61 12 16 D1         [24] 1550 	lcall	__gptrget
      000B64 90 80 1A         [24] 1551 	mov	dptr,#_enter_promiscuous_mode_PARM_2
      000B67 F0               [24] 1552 	movx	@dptr,a
      000B68 89 82            [24] 1553 	mov	dpl,r1
      000B6A 8A 83            [24] 1554 	mov	dph,r2
      000B6C 8B F0            [24] 1555 	mov	b,r3
      000B6E 02 04 C8         [24] 1556 	ljmp	_enter_promiscuous_mode
      000B71                       1557 00198$:
                                   1558 ;	src/radio.c:234: else if(request == ENTER_PROMISCUOUS_MODE_GENERIC)
      000B71 BF 0D 61         [24] 1559 	cjne	r7,#0x0d,00195$
                                   1560 ;	src/radio.c:236: enter_promiscuous_mode_generic(&data[3] /* address prefix */, data[0] /* prefix length */, data[1] /* rate */, data[2] /* payload length */);
      000B74 90 80 45         [24] 1561 	mov	dptr,#_handle_radio_request_PARM_2
      000B77 E0               [24] 1562 	movx	a,@dptr
      000B78 FC               [12] 1563 	mov	r4,a
      000B79 A3               [24] 1564 	inc	dptr
      000B7A E0               [24] 1565 	movx	a,@dptr
      000B7B FD               [12] 1566 	mov	r5,a
      000B7C A3               [24] 1567 	inc	dptr
      000B7D E0               [24] 1568 	movx	a,@dptr
      000B7E FE               [12] 1569 	mov	r6,a
      000B7F 74 03            [12] 1570 	mov	a,#0x03
      000B81 2C               [12] 1571 	add	a,r4
      000B82 F5 2F            [12] 1572 	mov	_handle_radio_request_sloc1_1_0,a
      000B84 E4               [12] 1573 	clr	a
      000B85 3D               [12] 1574 	addc	a,r5
      000B86 F5 30            [12] 1575 	mov	(_handle_radio_request_sloc1_1_0 + 1),a
      000B88 8E 31            [24] 1576 	mov	(_handle_radio_request_sloc1_1_0 + 2),r6
      000B8A 8C 82            [24] 1577 	mov	dpl,r4
      000B8C 8D 83            [24] 1578 	mov	dph,r5
      000B8E 8E F0            [24] 1579 	mov	b,r6
      000B90 12 16 D1         [24] 1580 	lcall	__gptrget
      000B93 F5 2E            [12] 1581 	mov	_handle_radio_request_sloc0_1_0,a
      000B95 74 01            [12] 1582 	mov	a,#0x01
      000B97 2C               [12] 1583 	add	a,r4
      000B98 F8               [12] 1584 	mov	r0,a
      000B99 E4               [12] 1585 	clr	a
      000B9A 3D               [12] 1586 	addc	a,r5
      000B9B FA               [12] 1587 	mov	r2,a
      000B9C 8E 03            [24] 1588 	mov	ar3,r6
      000B9E 88 82            [24] 1589 	mov	dpl,r0
      000BA0 8A 83            [24] 1590 	mov	dph,r2
      000BA2 8B F0            [24] 1591 	mov	b,r3
      000BA4 12 16 D1         [24] 1592 	lcall	__gptrget
      000BA7 F8               [12] 1593 	mov	r0,a
      000BA8 74 02            [12] 1594 	mov	a,#0x02
      000BAA 2C               [12] 1595 	add	a,r4
      000BAB FC               [12] 1596 	mov	r4,a
      000BAC E4               [12] 1597 	clr	a
      000BAD 3D               [12] 1598 	addc	a,r5
      000BAE FD               [12] 1599 	mov	r5,a
      000BAF 8C 82            [24] 1600 	mov	dpl,r4
      000BB1 8D 83            [24] 1601 	mov	dph,r5
      000BB3 8E F0            [24] 1602 	mov	b,r6
      000BB5 12 16 D1         [24] 1603 	lcall	__gptrget
      000BB8 FC               [12] 1604 	mov	r4,a
      000BB9 90 80 20         [24] 1605 	mov	dptr,#_enter_promiscuous_mode_generic_PARM_2
      000BBC E5 2E            [12] 1606 	mov	a,_handle_radio_request_sloc0_1_0
      000BBE F0               [24] 1607 	movx	@dptr,a
      000BBF 90 80 21         [24] 1608 	mov	dptr,#_enter_promiscuous_mode_generic_PARM_3
      000BC2 E8               [12] 1609 	mov	a,r0
      000BC3 F0               [24] 1610 	movx	@dptr,a
      000BC4 90 80 22         [24] 1611 	mov	dptr,#_enter_promiscuous_mode_generic_PARM_4
      000BC7 EC               [12] 1612 	mov	a,r4
      000BC8 F0               [24] 1613 	movx	@dptr,a
      000BC9 85 2F 82         [24] 1614 	mov	dpl,_handle_radio_request_sloc1_1_0
      000BCC 85 30 83         [24] 1615 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      000BCF 85 31 F0         [24] 1616 	mov	b,(_handle_radio_request_sloc1_1_0 + 2)
      000BD2 02 06 04         [24] 1617 	ljmp	_enter_promiscuous_mode_generic
      000BD5                       1618 00195$:
                                   1619 ;	src/radio.c:240: else if(request == ENTER_TONE_TEST_MODE)
      000BD5 BF 07 17         [24] 1620 	cjne	r7,#0x07,00192$
                                   1621 ;	src/radio.c:242: configure_phy(PWR_UP, CONT_WAVE | PLL_LOCK, 0);
      000BD8 90 80 2F         [24] 1622 	mov	dptr,#_configure_phy_PARM_2
      000BDB 74 90            [12] 1623 	mov	a,#0x90
      000BDD F0               [24] 1624 	movx	@dptr,a
      000BDE 90 80 30         [24] 1625 	mov	dptr,#_configure_phy_PARM_3
      000BE1 E4               [12] 1626 	clr	a
      000BE2 F0               [24] 1627 	movx	@dptr,a
      000BE3 75 82 02         [24] 1628 	mov	dpl,#0x02
      000BE6 12 08 24         [24] 1629 	lcall	_configure_phy
                                   1630 ;	src/radio.c:243: in1bc = 0;
      000BE9 90 C7 B7         [24] 1631 	mov	dptr,#0xc7b7
      000BEC E4               [12] 1632 	clr	a
      000BED F0               [24] 1633 	movx	@dptr,a
                                   1634 ;	src/radio.c:244: return;
      000BEE 22               [24] 1635 	ret
      000BEF                       1636 00192$:
                                   1637 ;	src/radio.c:248: else if(request == RECEIVE_PACKET)
      000BEF BF 12 02         [24] 1638 	cjne	r7,#0x12,00528$
      000BF2 80 03            [24] 1639 	sjmp	00529$
      000BF4                       1640 00528$:
      000BF4 02 10 BA         [24] 1641 	ljmp	00189$
      000BF7                       1642 00529$:
                                   1643 ;	src/radio.c:253: read_register(FIFO_STATUS, &value, 1);
      000BF7 90 80 38         [24] 1644 	mov	dptr,#_spi_read_PARM_2
      000BFA 74 52            [12] 1645 	mov	a,#_handle_radio_request_value_131072_79
      000BFC F0               [24] 1646 	movx	@dptr,a
      000BFD 74 80            [12] 1647 	mov	a,#(_handle_radio_request_value_131072_79 >> 8)
      000BFF A3               [24] 1648 	inc	dptr
      000C00 F0               [24] 1649 	movx	@dptr,a
      000C01 E4               [12] 1650 	clr	a
      000C02 A3               [24] 1651 	inc	dptr
      000C03 F0               [24] 1652 	movx	@dptr,a
      000C04 90 80 3B         [24] 1653 	mov	dptr,#_spi_read_PARM_3
      000C07 04               [12] 1654 	inc	a
      000C08 F0               [24] 1655 	movx	@dptr,a
      000C09 75 82 17         [24] 1656 	mov	dpl,#0x17
      000C0C 12 08 D7         [24] 1657 	lcall	_spi_read
                                   1658 ;	src/radio.c:254: if((value & 1) == 0)
      000C0F 90 80 52         [24] 1659 	mov	dptr,#_handle_radio_request_value_131072_79
      000C12 E0               [24] 1660 	movx	a,@dptr
      000C13 30 E0 03         [24] 1661 	jnb	acc.0,00530$
      000C16 02 10 AD         [24] 1662 	ljmp	00133$
      000C19                       1663 00530$:
                                   1664 ;	src/radio.c:257: if(radio_mode == sniffer)
      000C19 90 80 11         [24] 1665 	mov	dptr,#_radio_mode
      000C1C E0               [24] 1666 	movx	a,@dptr
      000C1D FE               [12] 1667 	mov	r6,a
      000C1E 70 7B            [24] 1668 	jnz	00130$
                                   1669 ;	src/radio.c:260: read_register(R_RX_PL_WID, &value, 1);
      000C20 90 80 38         [24] 1670 	mov	dptr,#_spi_read_PARM_2
      000C23 74 52            [12] 1671 	mov	a,#_handle_radio_request_value_131072_79
      000C25 F0               [24] 1672 	movx	@dptr,a
      000C26 74 80            [12] 1673 	mov	a,#(_handle_radio_request_value_131072_79 >> 8)
      000C28 A3               [24] 1674 	inc	dptr
      000C29 F0               [24] 1675 	movx	@dptr,a
      000C2A E4               [12] 1676 	clr	a
      000C2B A3               [24] 1677 	inc	dptr
      000C2C F0               [24] 1678 	movx	@dptr,a
      000C2D 90 80 3B         [24] 1679 	mov	dptr,#_spi_read_PARM_3
      000C30 04               [12] 1680 	inc	a
      000C31 F0               [24] 1681 	movx	@dptr,a
      000C32 75 82 60         [24] 1682 	mov	dpl,#0x60
      000C35 12 08 D7         [24] 1683 	lcall	_spi_read
                                   1684 ;	src/radio.c:261: if(value <= 32)
      000C38 90 80 52         [24] 1685 	mov	dptr,#_handle_radio_request_value_131072_79
      000C3B E0               [24] 1686 	movx	a,@dptr
      000C3C FD               [12] 1687 	mov  r5,a
      000C3D 24 DF            [12] 1688 	add	a,#0xff - 0x20
      000C3F 40 3B            [24] 1689 	jc	00105$
                                   1690 ;	src/radio.c:264: read_register(R_RX_PAYLOAD, &in1buf[1], value);
      000C41 90 80 38         [24] 1691 	mov	dptr,#_spi_read_PARM_2
      000C44 74 81            [12] 1692 	mov	a,#(_in1buf + 0x0001)
      000C46 F0               [24] 1693 	movx	@dptr,a
      000C47 74 C6            [12] 1694 	mov	a,#((_in1buf + 0x0001) >> 8)
      000C49 A3               [24] 1695 	inc	dptr
      000C4A F0               [24] 1696 	movx	@dptr,a
      000C4B E4               [12] 1697 	clr	a
      000C4C A3               [24] 1698 	inc	dptr
      000C4D F0               [24] 1699 	movx	@dptr,a
      000C4E 90 80 3B         [24] 1700 	mov	dptr,#_spi_read_PARM_3
      000C51 ED               [12] 1701 	mov	a,r5
      000C52 F0               [24] 1702 	movx	@dptr,a
      000C53 75 82 61         [24] 1703 	mov	dpl,#0x61
      000C56 12 08 D7         [24] 1704 	lcall	_spi_read
                                   1705 ;	src/radio.c:265: in1buf[0] = 0;
      000C59 90 C6 80         [24] 1706 	mov	dptr,#_in1buf
      000C5C E4               [12] 1707 	clr	a
      000C5D F0               [24] 1708 	movx	@dptr,a
                                   1709 ;	src/radio.c:266: in1bc = value + 1;
      000C5E 90 80 52         [24] 1710 	mov	dptr,#_handle_radio_request_value_131072_79
      000C61 E0               [24] 1711 	movx	a,@dptr
      000C62 FD               [12] 1712 	mov	r5,a
      000C63 0D               [12] 1713 	inc	r5
      000C64 90 C7 B7         [24] 1714 	mov	dptr,#0xc7b7
      000C67 ED               [12] 1715 	mov	a,r5
      000C68 F0               [24] 1716 	movx	@dptr,a
                                   1717 ;	src/radio.c:267: flush_rx();
      000C69 90 80 33         [24] 1718 	mov	dptr,#_spi_write_PARM_2
      000C6C E4               [12] 1719 	clr	a
      000C6D F0               [24] 1720 	movx	@dptr,a
      000C6E A3               [24] 1721 	inc	dptr
      000C6F F0               [24] 1722 	movx	@dptr,a
      000C70 A3               [24] 1723 	inc	dptr
      000C71 F0               [24] 1724 	movx	@dptr,a
      000C72 90 80 36         [24] 1725 	mov	dptr,#_spi_write_PARM_3
      000C75 F0               [24] 1726 	movx	@dptr,a
      000C76 75 82 E2         [24] 1727 	mov	dpl,#0xe2
                                   1728 ;	src/radio.c:268: return;
      000C79 02 08 63         [24] 1729 	ljmp	_spi_write
      000C7C                       1730 00105$:
                                   1731 ;	src/radio.c:273: in1bc = 1;
      000C7C 90 C7 B7         [24] 1732 	mov	dptr,#0xc7b7
      000C7F 74 01            [12] 1733 	mov	a,#0x01
      000C81 F0               [24] 1734 	movx	@dptr,a
                                   1735 ;	src/radio.c:274: in1buf[0] = 0xFF;
      000C82 90 C6 80         [24] 1736 	mov	dptr,#_in1buf
      000C85 74 FF            [12] 1737 	mov	a,#0xff
      000C87 F0               [24] 1738 	movx	@dptr,a
                                   1739 ;	src/radio.c:275: flush_rx();
      000C88 90 80 33         [24] 1740 	mov	dptr,#_spi_write_PARM_2
      000C8B E4               [12] 1741 	clr	a
      000C8C F0               [24] 1742 	movx	@dptr,a
      000C8D A3               [24] 1743 	inc	dptr
      000C8E F0               [24] 1744 	movx	@dptr,a
      000C8F A3               [24] 1745 	inc	dptr
      000C90 F0               [24] 1746 	movx	@dptr,a
      000C91 90 80 36         [24] 1747 	mov	dptr,#_spi_write_PARM_3
      000C94 F0               [24] 1748 	movx	@dptr,a
      000C95 75 82 E2         [24] 1749 	mov	dpl,#0xe2
                                   1750 ;	src/radio.c:276: return;
      000C98 02 08 63         [24] 1751 	ljmp	_spi_write
      000C9B                       1752 00130$:
                                   1753 ;	src/radio.c:281: else if(radio_mode == promiscuous)
      000C9B BE 01 02         [24] 1754 	cjne	r6,#0x01,00533$
      000C9E 80 03            [24] 1755 	sjmp	00534$
      000CA0                       1756 00533$:
      000CA0 02 0F F5         [24] 1757 	ljmp	00127$
      000CA3                       1758 00534$:
                                   1759 ;	src/radio.c:289: for(x = 0; x < pm_prefix_length; x++) payload[pm_prefix_length - x - 1] = pm_prefix[x];
      000CA3 7C 00            [12] 1760 	mov	r4,#0x00
      000CA5 7D 00            [12] 1761 	mov	r5,#0x00
      000CA7                       1762 00228$:
      000CA7 90 80 12         [24] 1763 	mov	dptr,#_pm_prefix_length
      000CAA E0               [24] 1764 	movx	a,@dptr
      000CAB FA               [12] 1765 	mov	r2,a
      000CAC A3               [24] 1766 	inc	dptr
      000CAD E0               [24] 1767 	movx	a,@dptr
      000CAE FB               [12] 1768 	mov	r3,a
      000CAF C3               [12] 1769 	clr	c
      000CB0 EC               [12] 1770 	mov	a,r4
      000CB1 9A               [12] 1771 	subb	a,r2
      000CB2 ED               [12] 1772 	mov	a,r5
      000CB3 64 80            [12] 1773 	xrl	a,#0x80
      000CB5 8B F0            [24] 1774 	mov	b,r3
      000CB7 63 F0 80         [24] 1775 	xrl	b,#0x80
      000CBA 95 F0            [12] 1776 	subb	a,b
      000CBC 50 30            [24] 1777 	jnc	00107$
      000CBE 8A 01            [24] 1778 	mov	ar1,r2
      000CC0 8C 00            [24] 1779 	mov	ar0,r4
      000CC2 E9               [12] 1780 	mov	a,r1
      000CC3 C3               [12] 1781 	clr	c
      000CC4 98               [12] 1782 	subb	a,r0
      000CC5 14               [12] 1783 	dec	a
      000CC6 F8               [12] 1784 	mov	r0,a
      000CC7 33               [12] 1785 	rlc	a
      000CC8 95 E0            [12] 1786 	subb	a,acc
      000CCA F9               [12] 1787 	mov	r1,a
      000CCB E8               [12] 1788 	mov	a,r0
      000CCC 24 57            [12] 1789 	add	a,#_handle_radio_request_payload_262144_84
      000CCE F5 2F            [12] 1790 	mov	_handle_radio_request_sloc1_1_0,a
      000CD0 E9               [12] 1791 	mov	a,r1
      000CD1 34 80            [12] 1792 	addc	a,#(_handle_radio_request_payload_262144_84 >> 8)
      000CD3 F5 30            [12] 1793 	mov	(_handle_radio_request_sloc1_1_0 + 1),a
      000CD5 EC               [12] 1794 	mov	a,r4
      000CD6 24 14            [12] 1795 	add	a,#_pm_prefix
      000CD8 F5 82            [12] 1796 	mov	dpl,a
      000CDA ED               [12] 1797 	mov	a,r5
      000CDB 34 80            [12] 1798 	addc	a,#(_pm_prefix >> 8)
      000CDD F5 83            [12] 1799 	mov	dph,a
      000CDF E0               [24] 1800 	movx	a,@dptr
      000CE0 85 2F 82         [24] 1801 	mov	dpl,_handle_radio_request_sloc1_1_0
      000CE3 85 30 83         [24] 1802 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      000CE6 F0               [24] 1803 	movx	@dptr,a
      000CE7 0C               [12] 1804 	inc	r4
      000CE8 BC 00 BC         [24] 1805 	cjne	r4,#0x00,00228$
      000CEB 0D               [12] 1806 	inc	r5
      000CEC 80 B9            [24] 1807 	sjmp	00228$
      000CEE                       1808 00107$:
                                   1809 ;	src/radio.c:290: read_register(R_RX_PAYLOAD, &payload[pm_prefix_length], pm_payload_length);
      000CEE EA               [12] 1810 	mov	a,r2
      000CEF 24 57            [12] 1811 	add	a,#_handle_radio_request_payload_262144_84
      000CF1 FA               [12] 1812 	mov	r2,a
      000CF2 EB               [12] 1813 	mov	a,r3
      000CF3 34 80            [12] 1814 	addc	a,#(_handle_radio_request_payload_262144_84 >> 8)
      000CF5 FB               [12] 1815 	mov	r3,a
      000CF6 7D 00            [12] 1816 	mov	r5,#0x00
      000CF8 90 80 19         [24] 1817 	mov	dptr,#_pm_payload_length
      000CFB E0               [24] 1818 	movx	a,@dptr
      000CFC FC               [12] 1819 	mov	r4,a
      000CFD 90 80 38         [24] 1820 	mov	dptr,#_spi_read_PARM_2
      000D00 EA               [12] 1821 	mov	a,r2
      000D01 F0               [24] 1822 	movx	@dptr,a
      000D02 EB               [12] 1823 	mov	a,r3
      000D03 A3               [24] 1824 	inc	dptr
      000D04 F0               [24] 1825 	movx	@dptr,a
      000D05 ED               [12] 1826 	mov	a,r5
      000D06 A3               [24] 1827 	inc	dptr
      000D07 F0               [24] 1828 	movx	@dptr,a
      000D08 90 80 3B         [24] 1829 	mov	dptr,#_spi_read_PARM_3
      000D0B EC               [12] 1830 	mov	a,r4
      000D0C F0               [24] 1831 	movx	@dptr,a
      000D0D 75 82 61         [24] 1832 	mov	dpl,#0x61
      000D10 12 08 D7         [24] 1833 	lcall	_spi_read
                                   1834 ;	src/radio.c:297: for(offset = 0; offset < 2; offset++)
      000D13 7C 00            [12] 1835 	mov	r4,#0x00
      000D15 7D 00            [12] 1836 	mov	r5,#0x00
      000D17                       1837 00238$:
                                   1838 ;	src/radio.c:300: if(offset == 1)
      000D17 BC 01 74         [24] 1839 	cjne	r4,#0x01,00113$
      000D1A BD 00 71         [24] 1840 	cjne	r5,#0x00,00113$
                                   1841 ;	src/radio.c:302: for(x = 31; x >= 0; x--)
      000D1D 7A 1F            [12] 1842 	mov	r2,#0x1f
      000D1F 7B 00            [12] 1843 	mov	r3,#0x00
      000D21                       1844 00230$:
                                   1845 ;	src/radio.c:304: if(x > 0) payload[x] = payload[x - 1] << 7 | payload[x] >> 1;
      000D21 C3               [12] 1846 	clr	c
      000D22 E4               [12] 1847 	clr	a
      000D23 9A               [12] 1848 	subb	a,r2
      000D24 74 80            [12] 1849 	mov	a,#(0x00 ^ 0x80)
      000D26 8B F0            [24] 1850 	mov	b,r3
      000D28 63 F0 80         [24] 1851 	xrl	b,#0x80
      000D2B 95 F0            [12] 1852 	subb	a,b
      000D2D 50 3A            [24] 1853 	jnc	00109$
      000D2F C0 04            [24] 1854 	push	ar4
      000D31 C0 05            [24] 1855 	push	ar5
      000D33 EA               [12] 1856 	mov	a,r2
      000D34 24 57            [12] 1857 	add	a,#_handle_radio_request_payload_262144_84
      000D36 F8               [12] 1858 	mov	r0,a
      000D37 EB               [12] 1859 	mov	a,r3
      000D38 34 80            [12] 1860 	addc	a,#(_handle_radio_request_payload_262144_84 >> 8)
      000D3A F9               [12] 1861 	mov	r1,a
      000D3B 8A 05            [24] 1862 	mov	ar5,r2
      000D3D 1D               [12] 1863 	dec	r5
      000D3E ED               [12] 1864 	mov	a,r5
      000D3F 33               [12] 1865 	rlc	a
      000D40 95 E0            [12] 1866 	subb	a,acc
      000D42 FC               [12] 1867 	mov	r4,a
      000D43 ED               [12] 1868 	mov	a,r5
      000D44 24 57            [12] 1869 	add	a,#_handle_radio_request_payload_262144_84
      000D46 F5 82            [12] 1870 	mov	dpl,a
      000D48 EC               [12] 1871 	mov	a,r4
      000D49 34 80            [12] 1872 	addc	a,#(_handle_radio_request_payload_262144_84 >> 8)
      000D4B F5 83            [12] 1873 	mov	dph,a
      000D4D E0               [24] 1874 	movx	a,@dptr
      000D4E 03               [12] 1875 	rr	a
      000D4F 54 80            [12] 1876 	anl	a,#0x80
      000D51 FD               [12] 1877 	mov	r5,a
      000D52 88 82            [24] 1878 	mov	dpl,r0
      000D54 89 83            [24] 1879 	mov	dph,r1
      000D56 E0               [24] 1880 	movx	a,@dptr
      000D57 C3               [12] 1881 	clr	c
      000D58 13               [12] 1882 	rrc	a
      000D59 FC               [12] 1883 	mov	r4,a
      000D5A ED               [12] 1884 	mov	a,r5
      000D5B 42 04            [12] 1885 	orl	ar4,a
      000D5D 88 82            [24] 1886 	mov	dpl,r0
      000D5F 89 83            [24] 1887 	mov	dph,r1
      000D61 EC               [12] 1888 	mov	a,r4
      000D62 F0               [24] 1889 	movx	@dptr,a
      000D63 D0 05            [24] 1890 	pop	ar5
      000D65 D0 04            [24] 1891 	pop	ar4
      000D67 80 1C            [24] 1892 	sjmp	00231$
      000D69                       1893 00109$:
                                   1894 ;	src/radio.c:305: else payload[x] = payload[x] >> 1;
      000D69 C0 04            [24] 1895 	push	ar4
      000D6B C0 05            [24] 1896 	push	ar5
      000D6D EA               [12] 1897 	mov	a,r2
      000D6E 24 57            [12] 1898 	add	a,#_handle_radio_request_payload_262144_84
      000D70 F8               [12] 1899 	mov	r0,a
      000D71 EB               [12] 1900 	mov	a,r3
      000D72 34 80            [12] 1901 	addc	a,#(_handle_radio_request_payload_262144_84 >> 8)
      000D74 F9               [12] 1902 	mov	r1,a
      000D75 88 82            [24] 1903 	mov	dpl,r0
      000D77 89 83            [24] 1904 	mov	dph,r1
      000D79 E0               [24] 1905 	movx	a,@dptr
      000D7A C3               [12] 1906 	clr	c
      000D7B 13               [12] 1907 	rrc	a
      000D7C 88 82            [24] 1908 	mov	dpl,r0
      000D7E 89 83            [24] 1909 	mov	dph,r1
      000D80 F0               [24] 1910 	movx	@dptr,a
                                   1911 ;	src/radio.c:583: in1bc = 1;
      000D81 D0 05            [24] 1912 	pop	ar5
      000D83 D0 04            [24] 1913 	pop	ar4
                                   1914 ;	src/radio.c:305: else payload[x] = payload[x] >> 1;
      000D85                       1915 00231$:
                                   1916 ;	src/radio.c:302: for(x = 31; x >= 0; x--)
      000D85 1A               [12] 1917 	dec	r2
      000D86 BA FF 01         [24] 1918 	cjne	r2,#0xff,00540$
      000D89 1B               [12] 1919 	dec	r3
      000D8A                       1920 00540$:
      000D8A EB               [12] 1921 	mov	a,r3
      000D8B 30 E7 93         [24] 1922 	jnb	acc.7,00230$
      000D8E                       1923 00113$:
                                   1924 ;	src/radio.c:310: payload_length = payload[5] >> 2;
      000D8E C0 04            [24] 1925 	push	ar4
      000D90 C0 05            [24] 1926 	push	ar5
      000D92 90 80 5C         [24] 1927 	mov	dptr,#(_handle_radio_request_payload_262144_84 + 0x0005)
      000D95 E0               [24] 1928 	movx	a,@dptr
      000D96 03               [12] 1929 	rr	a
      000D97 03               [12] 1930 	rr	a
      000D98 54 3F            [12] 1931 	anl	a,#0x3f
      000D9A FB               [12] 1932 	mov	r3,a
                                   1933 ;	src/radio.c:315: if(payload_length <= (pm_payload_length-9) + pm_prefix_length)
      000D9B 90 80 19         [24] 1934 	mov	dptr,#_pm_payload_length
      000D9E E0               [24] 1935 	movx	a,@dptr
      000D9F 7A 00            [12] 1936 	mov	r2,#0x00
      000DA1 24 F7            [12] 1937 	add	a,#0xf7
      000DA3 F9               [12] 1938 	mov	r1,a
      000DA4 EA               [12] 1939 	mov	a,r2
      000DA5 34 FF            [12] 1940 	addc	a,#0xff
      000DA7 FA               [12] 1941 	mov	r2,a
      000DA8 90 80 12         [24] 1942 	mov	dptr,#_pm_prefix_length
      000DAB E0               [24] 1943 	movx	a,@dptr
      000DAC F8               [12] 1944 	mov	r0,a
      000DAD A3               [24] 1945 	inc	dptr
      000DAE E0               [24] 1946 	movx	a,@dptr
      000DAF FD               [12] 1947 	mov	r5,a
      000DB0 E8               [12] 1948 	mov	a,r0
      000DB1 29               [12] 1949 	add	a,r1
      000DB2 F9               [12] 1950 	mov	r1,a
      000DB3 ED               [12] 1951 	mov	a,r5
      000DB4 3A               [12] 1952 	addc	a,r2
      000DB5 FA               [12] 1953 	mov	r2,a
      000DB6 8B 2F            [24] 1954 	mov	_handle_radio_request_sloc1_1_0,r3
      000DB8 75 30 00         [24] 1955 	mov	(_handle_radio_request_sloc1_1_0 + 1),#0x00
      000DBB C3               [12] 1956 	clr	c
      000DBC E9               [12] 1957 	mov	a,r1
      000DBD 95 2F            [12] 1958 	subb	a,_handle_radio_request_sloc1_1_0
      000DBF EA               [12] 1959 	mov	a,r2
      000DC0 64 80            [12] 1960 	xrl	a,#0x80
      000DC2 85 30 F0         [24] 1961 	mov	b,(_handle_radio_request_sloc1_1_0 + 1)
      000DC5 63 F0 80         [24] 1962 	xrl	b,#0x80
      000DC8 95 F0            [12] 1963 	subb	a,b
      000DCA D0 05            [24] 1964 	pop	ar5
      000DCC D0 04            [24] 1965 	pop	ar4
      000DCE 50 03            [24] 1966 	jnc	00542$
      000DD0 02 0F DF         [24] 1967 	ljmp	00239$
      000DD3                       1968 00542$:
                                   1969 ;	src/radio.c:318: crc_given = (payload[6 + payload_length] << 9) | ((payload[7 + payload_length]) << 1);
      000DD3 C0 04            [24] 1970 	push	ar4
      000DD5 C0 05            [24] 1971 	push	ar5
      000DD7 74 06            [12] 1972 	mov	a,#0x06
      000DD9 2B               [12] 1973 	add	a,r3
      000DDA F9               [12] 1974 	mov	r1,a
      000DDB 33               [12] 1975 	rlc	a
      000DDC 95 E0            [12] 1976 	subb	a,acc
      000DDE FA               [12] 1977 	mov	r2,a
      000DDF E9               [12] 1978 	mov	a,r1
      000DE0 24 57            [12] 1979 	add	a,#_handle_radio_request_payload_262144_84
      000DE2 F5 82            [12] 1980 	mov	dpl,a
      000DE4 EA               [12] 1981 	mov	a,r2
      000DE5 34 80            [12] 1982 	addc	a,#(_handle_radio_request_payload_262144_84 >> 8)
      000DE7 F5 83            [12] 1983 	mov	dph,a
      000DE9 E0               [24] 1984 	movx	a,@dptr
      000DEA F9               [12] 1985 	mov	r1,a
      000DEB 7A 00            [12] 1986 	mov	r2,#0x00
      000DED 29               [12] 1987 	add	a,r1
      000DEE CA               [12] 1988 	xch	a,r2
      000DEF 79 00            [12] 1989 	mov	r1,#0x00
      000DF1 74 07            [12] 1990 	mov	a,#0x07
      000DF3 2B               [12] 1991 	add	a,r3
      000DF4 F8               [12] 1992 	mov	r0,a
      000DF5 33               [12] 1993 	rlc	a
      000DF6 95 E0            [12] 1994 	subb	a,acc
      000DF8 FD               [12] 1995 	mov	r5,a
      000DF9 E8               [12] 1996 	mov	a,r0
      000DFA 24 57            [12] 1997 	add	a,#_handle_radio_request_payload_262144_84
      000DFC F5 82            [12] 1998 	mov	dpl,a
      000DFE ED               [12] 1999 	mov	a,r5
      000DFF 34 80            [12] 2000 	addc	a,#(_handle_radio_request_payload_262144_84 >> 8)
      000E01 F5 83            [12] 2001 	mov	dph,a
      000E03 E0               [24] 2002 	movx	a,@dptr
      000E04 7C 00            [12] 2003 	mov	r4,#0x00
      000E06 25 E0            [12] 2004 	add	a,acc
      000E08 FD               [12] 2005 	mov	r5,a
      000E09 EC               [12] 2006 	mov	a,r4
      000E0A 33               [12] 2007 	rlc	a
      000E0B FC               [12] 2008 	mov	r4,a
      000E0C ED               [12] 2009 	mov	a,r5
      000E0D 42 01            [12] 2010 	orl	ar1,a
      000E0F EC               [12] 2011 	mov	a,r4
      000E10 42 02            [12] 2012 	orl	ar2,a
                                   2013 ;	src/radio.c:319: crc_given = (crc_given << 8) | (crc_given >> 8);
      000E12 8A 32            [24] 2014 	mov	_handle_radio_request_sloc2_1_0,r2
      000E14 89 33            [24] 2015 	mov	(_handle_radio_request_sloc2_1_0 + 1),r1
      000E16 90 80 55         [24] 2016 	mov	dptr,#_handle_radio_request_crc_given_262144_84
      000E19 E5 32            [12] 2017 	mov	a,_handle_radio_request_sloc2_1_0
      000E1B F0               [24] 2018 	movx	@dptr,a
      000E1C E5 33            [12] 2019 	mov	a,(_handle_radio_request_sloc2_1_0 + 1)
      000E1E A3               [24] 2020 	inc	dptr
      000E1F F0               [24] 2021 	movx	@dptr,a
                                   2022 ;	src/radio.c:320: if(payload[8 + payload_length] & 0x80) crc_given |= 0x100;
      000E20 74 08            [12] 2023 	mov	a,#0x08
      000E22 2B               [12] 2024 	add	a,r3
      000E23 FD               [12] 2025 	mov	r5,a
      000E24 33               [12] 2026 	rlc	a
      000E25 95 E0            [12] 2027 	subb	a,acc
      000E27 FC               [12] 2028 	mov	r4,a
      000E28 ED               [12] 2029 	mov	a,r5
      000E29 24 57            [12] 2030 	add	a,#_handle_radio_request_payload_262144_84
      000E2B F5 82            [12] 2031 	mov	dpl,a
      000E2D EC               [12] 2032 	mov	a,r4
      000E2E 34 80            [12] 2033 	addc	a,#(_handle_radio_request_payload_262144_84 >> 8)
      000E30 F5 83            [12] 2034 	mov	dph,a
      000E32 E0               [24] 2035 	movx	a,@dptr
      000E33 D0 05            [24] 2036 	pop	ar5
      000E35 D0 04            [24] 2037 	pop	ar4
      000E37 30 E7 0F         [24] 2038 	jnb	acc.7,00115$
      000E3A A9 32            [24] 2039 	mov	r1,_handle_radio_request_sloc2_1_0
      000E3C AA 33            [24] 2040 	mov	r2,(_handle_radio_request_sloc2_1_0 + 1)
      000E3E 43 02 01         [24] 2041 	orl	ar2,#0x01
      000E41 90 80 55         [24] 2042 	mov	dptr,#_handle_radio_request_crc_given_262144_84
      000E44 E9               [12] 2043 	mov	a,r1
      000E45 F0               [24] 2044 	movx	@dptr,a
      000E46 EA               [12] 2045 	mov	a,r2
      000E47 A3               [24] 2046 	inc	dptr
      000E48 F0               [24] 2047 	movx	@dptr,a
      000E49                       2048 00115$:
                                   2049 ;	src/radio.c:323: crc = 0xFFFF;
      000E49 90 80 53         [24] 2050 	mov	dptr,#_handle_radio_request_crc_262144_84
      000E4C 74 FF            [12] 2051 	mov	a,#0xff
      000E4E F0               [24] 2052 	movx	@dptr,a
      000E4F A3               [24] 2053 	inc	dptr
      000E50 F0               [24] 2054 	movx	@dptr,a
                                   2055 ;	src/radio.c:324: for(x = 0; x < 6 + payload_length; x++) crc = crc_update(crc, payload[x], 8);
      000E51 74 06            [12] 2056 	mov	a,#0x06
      000E53 25 2F            [12] 2057 	add	a,_handle_radio_request_sloc1_1_0
      000E55 F9               [12] 2058 	mov	r1,a
      000E56 E4               [12] 2059 	clr	a
      000E57 35 30            [12] 2060 	addc	a,(_handle_radio_request_sloc1_1_0 + 1)
      000E59 FA               [12] 2061 	mov	r2,a
      000E5A E4               [12] 2062 	clr	a
      000E5B F5 32            [12] 2063 	mov	_handle_radio_request_sloc2_1_0,a
      000E5D F5 33            [12] 2064 	mov	(_handle_radio_request_sloc2_1_0 + 1),a
      000E5F                       2065 00233$:
      000E5F C3               [12] 2066 	clr	c
      000E60 E5 32            [12] 2067 	mov	a,_handle_radio_request_sloc2_1_0
      000E62 99               [12] 2068 	subb	a,r1
      000E63 E5 33            [12] 2069 	mov	a,(_handle_radio_request_sloc2_1_0 + 1)
      000E65 64 80            [12] 2070 	xrl	a,#0x80
      000E67 8A F0            [24] 2071 	mov	b,r2
      000E69 63 F0 80         [24] 2072 	xrl	b,#0x80
      000E6C 95 F0            [12] 2073 	subb	a,b
      000E6E 50 5A            [24] 2074 	jnc	00116$
      000E70 C0 04            [24] 2075 	push	ar4
      000E72 C0 05            [24] 2076 	push	ar5
      000E74 90 80 53         [24] 2077 	mov	dptr,#_handle_radio_request_crc_262144_84
      000E77 E0               [24] 2078 	movx	a,@dptr
      000E78 F8               [12] 2079 	mov	r0,a
      000E79 A3               [24] 2080 	inc	dptr
      000E7A E0               [24] 2081 	movx	a,@dptr
      000E7B FD               [12] 2082 	mov	r5,a
      000E7C E5 32            [12] 2083 	mov	a,_handle_radio_request_sloc2_1_0
      000E7E 24 57            [12] 2084 	add	a,#_handle_radio_request_payload_262144_84
      000E80 F5 82            [12] 2085 	mov	dpl,a
      000E82 E5 33            [12] 2086 	mov	a,(_handle_radio_request_sloc2_1_0 + 1)
      000E84 34 80            [12] 2087 	addc	a,#(_handle_radio_request_payload_262144_84 >> 8)
      000E86 F5 83            [12] 2088 	mov	dph,a
      000E88 E0               [24] 2089 	movx	a,@dptr
      000E89 FC               [12] 2090 	mov	r4,a
      000E8A 90 80 41         [24] 2091 	mov	dptr,#_crc_update_PARM_2
      000E8D F0               [24] 2092 	movx	@dptr,a
      000E8E 90 80 42         [24] 2093 	mov	dptr,#_crc_update_PARM_3
      000E91 74 08            [12] 2094 	mov	a,#0x08
      000E93 F0               [24] 2095 	movx	@dptr,a
      000E94 88 82            [24] 2096 	mov	dpl,r0
      000E96 8D 83            [24] 2097 	mov	dph,r5
      000E98 C0 05            [24] 2098 	push	ar5
      000E9A C0 04            [24] 2099 	push	ar4
      000E9C C0 03            [24] 2100 	push	ar3
      000E9E C0 02            [24] 2101 	push	ar2
      000EA0 C0 01            [24] 2102 	push	ar1
      000EA2 12 09 97         [24] 2103 	lcall	_crc_update
      000EA5 E5 82            [12] 2104 	mov	a,dpl
      000EA7 85 83 F0         [24] 2105 	mov	b,dph
      000EAA D0 01            [24] 2106 	pop	ar1
      000EAC D0 02            [24] 2107 	pop	ar2
      000EAE D0 03            [24] 2108 	pop	ar3
      000EB0 D0 04            [24] 2109 	pop	ar4
      000EB2 D0 05            [24] 2110 	pop	ar5
      000EB4 90 80 53         [24] 2111 	mov	dptr,#_handle_radio_request_crc_262144_84
      000EB7 F0               [24] 2112 	movx	@dptr,a
      000EB8 E5 F0            [12] 2113 	mov	a,b
      000EBA A3               [24] 2114 	inc	dptr
      000EBB F0               [24] 2115 	movx	@dptr,a
      000EBC 05 32            [12] 2116 	inc	_handle_radio_request_sloc2_1_0
      000EBE E4               [12] 2117 	clr	a
      000EBF B5 32 02         [24] 2118 	cjne	a,_handle_radio_request_sloc2_1_0,00545$
      000EC2 05 33            [12] 2119 	inc	(_handle_radio_request_sloc2_1_0 + 1)
      000EC4                       2120 00545$:
      000EC4 D0 05            [24] 2121 	pop	ar5
      000EC6 D0 04            [24] 2122 	pop	ar4
      000EC8 80 95            [24] 2123 	sjmp	00233$
      000ECA                       2124 00116$:
                                   2125 ;	src/radio.c:325: crc = crc_update(crc, payload[6 + payload_length] & 0x80, 1);
      000ECA C0 04            [24] 2126 	push	ar4
      000ECC C0 05            [24] 2127 	push	ar5
      000ECE 90 80 53         [24] 2128 	mov	dptr,#_handle_radio_request_crc_262144_84
      000ED1 E0               [24] 2129 	movx	a,@dptr
      000ED2 F9               [12] 2130 	mov	r1,a
      000ED3 A3               [24] 2131 	inc	dptr
      000ED4 E0               [24] 2132 	movx	a,@dptr
      000ED5 FA               [12] 2133 	mov	r2,a
      000ED6 74 06            [12] 2134 	mov	a,#0x06
      000ED8 2B               [12] 2135 	add	a,r3
      000ED9 F8               [12] 2136 	mov	r0,a
      000EDA 33               [12] 2137 	rlc	a
      000EDB 95 E0            [12] 2138 	subb	a,acc
      000EDD FD               [12] 2139 	mov	r5,a
      000EDE E8               [12] 2140 	mov	a,r0
      000EDF 24 57            [12] 2141 	add	a,#_handle_radio_request_payload_262144_84
      000EE1 F5 82            [12] 2142 	mov	dpl,a
      000EE3 ED               [12] 2143 	mov	a,r5
      000EE4 34 80            [12] 2144 	addc	a,#(_handle_radio_request_payload_262144_84 >> 8)
      000EE6 F5 83            [12] 2145 	mov	dph,a
      000EE8 E0               [24] 2146 	movx	a,@dptr
      000EE9 FD               [12] 2147 	mov	r5,a
      000EEA 90 80 41         [24] 2148 	mov	dptr,#_crc_update_PARM_2
      000EED 74 80            [12] 2149 	mov	a,#0x80
      000EEF 5D               [12] 2150 	anl	a,r5
      000EF0 F0               [24] 2151 	movx	@dptr,a
      000EF1 90 80 42         [24] 2152 	mov	dptr,#_crc_update_PARM_3
      000EF4 74 01            [12] 2153 	mov	a,#0x01
      000EF6 F0               [24] 2154 	movx	@dptr,a
      000EF7 89 82            [24] 2155 	mov	dpl,r1
      000EF9 8A 83            [24] 2156 	mov	dph,r2
      000EFB C0 03            [24] 2157 	push	ar3
      000EFD 12 09 97         [24] 2158 	lcall	_crc_update
      000F00 AC 82            [24] 2159 	mov	r4,dpl
      000F02 AD 83            [24] 2160 	mov	r5,dph
      000F04 D0 03            [24] 2161 	pop	ar3
                                   2162 ;	src/radio.c:326: crc = (crc << 8) | (crc >> 8);
      000F06 EC               [12] 2163 	mov	a,r4
      000F07 8D 04            [24] 2164 	mov	ar4,r5
      000F09 FD               [12] 2165 	mov	r5,a
                                   2166 ;	src/radio.c:329: if(crc == crc_given)
      000F0A 90 80 55         [24] 2167 	mov	dptr,#_handle_radio_request_crc_given_262144_84
      000F0D E0               [24] 2168 	movx	a,@dptr
      000F0E F9               [12] 2169 	mov	r1,a
      000F0F A3               [24] 2170 	inc	dptr
      000F10 E0               [24] 2171 	movx	a,@dptr
      000F11 FA               [12] 2172 	mov	r2,a
      000F12 EC               [12] 2173 	mov	a,r4
      000F13 B5 01 06         [24] 2174 	cjne	a,ar1,00546$
      000F16 ED               [12] 2175 	mov	a,r5
      000F17 B5 02 02         [24] 2176 	cjne	a,ar2,00546$
      000F1A 80 07            [24] 2177 	sjmp	00547$
      000F1C                       2178 00546$:
      000F1C D0 05            [24] 2179 	pop	ar5
      000F1E D0 04            [24] 2180 	pop	ar4
      000F20 02 0F DF         [24] 2181 	ljmp	00239$
      000F23                       2182 00547$:
      000F23 D0 05            [24] 2183 	pop	ar5
      000F25 D0 04            [24] 2184 	pop	ar4
                                   2185 ;	src/radio.c:332: memcpy(in1buf, payload, 5);
      000F27 90 80 A1         [24] 2186 	mov	dptr,#___memcpy_PARM_2
      000F2A 74 57            [12] 2187 	mov	a,#_handle_radio_request_payload_262144_84
      000F2C F0               [24] 2188 	movx	@dptr,a
      000F2D 74 80            [12] 2189 	mov	a,#(_handle_radio_request_payload_262144_84 >> 8)
      000F2F A3               [24] 2190 	inc	dptr
      000F30 F0               [24] 2191 	movx	@dptr,a
      000F31 E4               [12] 2192 	clr	a
      000F32 A3               [24] 2193 	inc	dptr
      000F33 F0               [24] 2194 	movx	@dptr,a
      000F34 90 80 A4         [24] 2195 	mov	dptr,#___memcpy_PARM_3
      000F37 74 05            [12] 2196 	mov	a,#0x05
      000F39 F0               [24] 2197 	movx	@dptr,a
      000F3A E4               [12] 2198 	clr	a
      000F3B A3               [24] 2199 	inc	dptr
      000F3C F0               [24] 2200 	movx	@dptr,a
      000F3D 90 C6 80         [24] 2201 	mov	dptr,#_in1buf
      000F40 75 F0 00         [24] 2202 	mov	b,#0x00
      000F43 C0 03            [24] 2203 	push	ar3
      000F45 12 16 02         [24] 2204 	lcall	___memcpy
      000F48 D0 03            [24] 2205 	pop	ar3
                                   2206 ;	src/radio.c:335: for(x = 0; x < payload_length + 3; x++)
      000F4A 74 03            [12] 2207 	mov	a,#0x03
      000F4C 25 2F            [12] 2208 	add	a,_handle_radio_request_sloc1_1_0
      000F4E F9               [12] 2209 	mov	r1,a
      000F4F E4               [12] 2210 	clr	a
      000F50 35 30            [12] 2211 	addc	a,(_handle_radio_request_sloc1_1_0 + 1)
      000F52 FA               [12] 2212 	mov	r2,a
      000F53 E4               [12] 2213 	clr	a
      000F54 F5 32            [12] 2214 	mov	_handle_radio_request_sloc2_1_0,a
      000F56 F5 33            [12] 2215 	mov	(_handle_radio_request_sloc2_1_0 + 1),a
      000F58                       2216 00236$:
      000F58 C3               [12] 2217 	clr	c
      000F59 E5 32            [12] 2218 	mov	a,_handle_radio_request_sloc2_1_0
      000F5B 99               [12] 2219 	subb	a,r1
      000F5C E5 33            [12] 2220 	mov	a,(_handle_radio_request_sloc2_1_0 + 1)
      000F5E 64 80            [12] 2221 	xrl	a,#0x80
      000F60 8A F0            [24] 2222 	mov	b,r2
      000F62 63 F0 80         [24] 2223 	xrl	b,#0x80
      000F65 95 F0            [12] 2224 	subb	a,b
      000F67 50 5C            [24] 2225 	jnc	00117$
                                   2226 ;	src/radio.c:336: in1buf[5+x] = ((payload[6 + x] << 1) & 0xFF) | (payload[7 + x] >> 7);
      000F69 C0 01            [24] 2227 	push	ar1
      000F6B C0 02            [24] 2228 	push	ar2
      000F6D A8 32            [24] 2229 	mov	r0,_handle_radio_request_sloc2_1_0
      000F6F 74 05            [12] 2230 	mov	a,#0x05
      000F71 28               [12] 2231 	add	a,r0
      000F72 F9               [12] 2232 	mov	r1,a
      000F73 33               [12] 2233 	rlc	a
      000F74 95 E0            [12] 2234 	subb	a,acc
      000F76 FA               [12] 2235 	mov	r2,a
      000F77 E9               [12] 2236 	mov	a,r1
      000F78 24 80            [12] 2237 	add	a,#_in1buf
      000F7A F5 2F            [12] 2238 	mov	_handle_radio_request_sloc1_1_0,a
      000F7C EA               [12] 2239 	mov	a,r2
      000F7D 34 C6            [12] 2240 	addc	a,#(_in1buf >> 8)
      000F7F F5 30            [12] 2241 	mov	(_handle_radio_request_sloc1_1_0 + 1),a
      000F81 74 06            [12] 2242 	mov	a,#0x06
      000F83 28               [12] 2243 	add	a,r0
      000F84 F9               [12] 2244 	mov	r1,a
      000F85 33               [12] 2245 	rlc	a
      000F86 95 E0            [12] 2246 	subb	a,acc
      000F88 FA               [12] 2247 	mov	r2,a
      000F89 E9               [12] 2248 	mov	a,r1
      000F8A 24 57            [12] 2249 	add	a,#_handle_radio_request_payload_262144_84
      000F8C F5 82            [12] 2250 	mov	dpl,a
      000F8E EA               [12] 2251 	mov	a,r2
      000F8F 34 80            [12] 2252 	addc	a,#(_handle_radio_request_payload_262144_84 >> 8)
      000F91 F5 83            [12] 2253 	mov	dph,a
      000F93 E0               [24] 2254 	movx	a,@dptr
      000F94 25 E0            [12] 2255 	add	a,acc
      000F96 FA               [12] 2256 	mov	r2,a
      000F97 74 07            [12] 2257 	mov	a,#0x07
      000F99 28               [12] 2258 	add	a,r0
      000F9A F8               [12] 2259 	mov	r0,a
      000F9B 33               [12] 2260 	rlc	a
      000F9C 95 E0            [12] 2261 	subb	a,acc
      000F9E F9               [12] 2262 	mov	r1,a
      000F9F E8               [12] 2263 	mov	a,r0
      000FA0 24 57            [12] 2264 	add	a,#_handle_radio_request_payload_262144_84
      000FA2 F5 82            [12] 2265 	mov	dpl,a
      000FA4 E9               [12] 2266 	mov	a,r1
      000FA5 34 80            [12] 2267 	addc	a,#(_handle_radio_request_payload_262144_84 >> 8)
      000FA7 F5 83            [12] 2268 	mov	dph,a
      000FA9 E0               [24] 2269 	movx	a,@dptr
      000FAA 23               [12] 2270 	rl	a
      000FAB 54 01            [12] 2271 	anl	a,#0x01
      000FAD 42 02            [12] 2272 	orl	ar2,a
      000FAF 85 2F 82         [24] 2273 	mov	dpl,_handle_radio_request_sloc1_1_0
      000FB2 85 30 83         [24] 2274 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      000FB5 EA               [12] 2275 	mov	a,r2
      000FB6 F0               [24] 2276 	movx	@dptr,a
                                   2277 ;	src/radio.c:335: for(x = 0; x < payload_length + 3; x++)
      000FB7 05 32            [12] 2278 	inc	_handle_radio_request_sloc2_1_0
      000FB9 E4               [12] 2279 	clr	a
      000FBA B5 32 02         [24] 2280 	cjne	a,_handle_radio_request_sloc2_1_0,00549$
      000FBD 05 33            [12] 2281 	inc	(_handle_radio_request_sloc2_1_0 + 1)
      000FBF                       2282 00549$:
      000FBF D0 02            [24] 2283 	pop	ar2
      000FC1 D0 01            [24] 2284 	pop	ar1
      000FC3 80 93            [24] 2285 	sjmp	00236$
      000FC5                       2286 00117$:
                                   2287 ;	src/radio.c:337: in1bc = 5 + payload_length;
      000FC5 74 05            [12] 2288 	mov	a,#0x05
      000FC7 2B               [12] 2289 	add	a,r3
      000FC8 90 C7 B7         [24] 2290 	mov	dptr,#0xc7b7
      000FCB F0               [24] 2291 	movx	@dptr,a
                                   2292 ;	src/radio.c:338: flush_rx();
      000FCC 90 80 33         [24] 2293 	mov	dptr,#_spi_write_PARM_2
      000FCF E4               [12] 2294 	clr	a
      000FD0 F0               [24] 2295 	movx	@dptr,a
      000FD1 A3               [24] 2296 	inc	dptr
      000FD2 F0               [24] 2297 	movx	@dptr,a
      000FD3 A3               [24] 2298 	inc	dptr
      000FD4 F0               [24] 2299 	movx	@dptr,a
      000FD5 90 80 36         [24] 2300 	mov	dptr,#_spi_write_PARM_3
      000FD8 F0               [24] 2301 	movx	@dptr,a
      000FD9 75 82 E2         [24] 2302 	mov	dpl,#0xe2
                                   2303 ;	src/radio.c:339: return;
      000FDC 02 08 63         [24] 2304 	ljmp	_spi_write
      000FDF                       2305 00239$:
                                   2306 ;	src/radio.c:297: for(offset = 0; offset < 2; offset++)
      000FDF 0C               [12] 2307 	inc	r4
      000FE0 BC 00 01         [24] 2308 	cjne	r4,#0x00,00550$
      000FE3 0D               [12] 2309 	inc	r5
      000FE4                       2310 00550$:
      000FE4 C3               [12] 2311 	clr	c
      000FE5 EC               [12] 2312 	mov	a,r4
      000FE6 94 02            [12] 2313 	subb	a,#0x02
      000FE8 ED               [12] 2314 	mov	a,r5
      000FE9 64 80            [12] 2315 	xrl	a,#0x80
      000FEB 94 80            [12] 2316 	subb	a,#0x80
      000FED 50 03            [24] 2317 	jnc	00551$
      000FEF 02 0D 17         [24] 2318 	ljmp	00238$
      000FF2                       2319 00551$:
      000FF2 02 10 AD         [24] 2320 	ljmp	00133$
      000FF5                       2321 00127$:
                                   2322 ;	src/radio.c:346: else if(radio_mode == promiscuous_generic)
      000FF5 BE 02 02         [24] 2323 	cjne	r6,#0x02,00552$
      000FF8 80 03            [24] 2324 	sjmp	00553$
      000FFA                       2325 00552$:
      000FFA 02 10 AD         [24] 2326 	ljmp	00133$
      000FFD                       2327 00553$:
                                   2328 ;	src/radio.c:352: for(x = 0; x < pm_prefix_length; x++) payload[pm_prefix_length - x - 1] = pm_prefix[x];
      000FFD 7D 00            [12] 2329 	mov	r5,#0x00
      000FFF 7E 00            [12] 2330 	mov	r6,#0x00
      001001                       2331 00241$:
      001001 90 80 12         [24] 2332 	mov	dptr,#_pm_prefix_length
      001004 E0               [24] 2333 	movx	a,@dptr
      001005 FB               [12] 2334 	mov	r3,a
      001006 A3               [24] 2335 	inc	dptr
      001007 E0               [24] 2336 	movx	a,@dptr
      001008 FC               [12] 2337 	mov	r4,a
      001009 C3               [12] 2338 	clr	c
      00100A ED               [12] 2339 	mov	a,r5
      00100B 9B               [12] 2340 	subb	a,r3
      00100C EE               [12] 2341 	mov	a,r6
      00100D 64 80            [12] 2342 	xrl	a,#0x80
      00100F 8C F0            [24] 2343 	mov	b,r4
      001011 63 F0 80         [24] 2344 	xrl	b,#0x80
      001014 95 F0            [12] 2345 	subb	a,b
      001016 50 2C            [24] 2346 	jnc	00123$
      001018 8B 02            [24] 2347 	mov	ar2,r3
      00101A 8D 01            [24] 2348 	mov	ar1,r5
      00101C EA               [12] 2349 	mov	a,r2
      00101D C3               [12] 2350 	clr	c
      00101E 99               [12] 2351 	subb	a,r1
      00101F 14               [12] 2352 	dec	a
      001020 F9               [12] 2353 	mov	r1,a
      001021 33               [12] 2354 	rlc	a
      001022 95 E0            [12] 2355 	subb	a,acc
      001024 FA               [12] 2356 	mov	r2,a
      001025 E9               [12] 2357 	mov	a,r1
      001026 24 7C            [12] 2358 	add	a,#_handle_radio_request_payload_262144_95
      001028 F9               [12] 2359 	mov	r1,a
      001029 EA               [12] 2360 	mov	a,r2
      00102A 34 80            [12] 2361 	addc	a,#(_handle_radio_request_payload_262144_95 >> 8)
      00102C FA               [12] 2362 	mov	r2,a
      00102D ED               [12] 2363 	mov	a,r5
      00102E 24 14            [12] 2364 	add	a,#_pm_prefix
      001030 F5 82            [12] 2365 	mov	dpl,a
      001032 EE               [12] 2366 	mov	a,r6
      001033 34 80            [12] 2367 	addc	a,#(_pm_prefix >> 8)
      001035 F5 83            [12] 2368 	mov	dph,a
      001037 E0               [24] 2369 	movx	a,@dptr
      001038 89 82            [24] 2370 	mov	dpl,r1
      00103A 8A 83            [24] 2371 	mov	dph,r2
      00103C F0               [24] 2372 	movx	@dptr,a
      00103D 0D               [12] 2373 	inc	r5
      00103E BD 00 C0         [24] 2374 	cjne	r5,#0x00,00241$
      001041 0E               [12] 2375 	inc	r6
      001042 80 BD            [24] 2376 	sjmp	00241$
      001044                       2377 00123$:
                                   2378 ;	src/radio.c:353: read_register(R_RX_PAYLOAD, &payload[pm_prefix_length], pm_payload_length);
      001044 EB               [12] 2379 	mov	a,r3
      001045 24 7C            [12] 2380 	add	a,#_handle_radio_request_payload_262144_95
      001047 FB               [12] 2381 	mov	r3,a
      001048 EC               [12] 2382 	mov	a,r4
      001049 34 80            [12] 2383 	addc	a,#(_handle_radio_request_payload_262144_95 >> 8)
      00104B FC               [12] 2384 	mov	r4,a
      00104C 7E 00            [12] 2385 	mov	r6,#0x00
      00104E 90 80 19         [24] 2386 	mov	dptr,#_pm_payload_length
      001051 E0               [24] 2387 	movx	a,@dptr
      001052 FD               [12] 2388 	mov	r5,a
      001053 90 80 38         [24] 2389 	mov	dptr,#_spi_read_PARM_2
      001056 EB               [12] 2390 	mov	a,r3
      001057 F0               [24] 2391 	movx	@dptr,a
      001058 EC               [12] 2392 	mov	a,r4
      001059 A3               [24] 2393 	inc	dptr
      00105A F0               [24] 2394 	movx	@dptr,a
      00105B EE               [12] 2395 	mov	a,r6
      00105C A3               [24] 2396 	inc	dptr
      00105D F0               [24] 2397 	movx	@dptr,a
      00105E 90 80 3B         [24] 2398 	mov	dptr,#_spi_read_PARM_3
      001061 ED               [12] 2399 	mov	a,r5
      001062 F0               [24] 2400 	movx	@dptr,a
      001063 75 82 61         [24] 2401 	mov	dpl,#0x61
      001066 12 08 D7         [24] 2402 	lcall	_spi_read
                                   2403 ;	src/radio.c:356: memcpy(in1buf, payload, pm_prefix_length + pm_payload_length);
      001069 90 80 19         [24] 2404 	mov	dptr,#_pm_payload_length
      00106C E0               [24] 2405 	movx	a,@dptr
      00106D FE               [12] 2406 	mov	r6,a
      00106E 7D 00            [12] 2407 	mov	r5,#0x00
      001070 90 80 12         [24] 2408 	mov	dptr,#_pm_prefix_length
      001073 E0               [24] 2409 	movx	a,@dptr
      001074 FB               [12] 2410 	mov	r3,a
      001075 A3               [24] 2411 	inc	dptr
      001076 E0               [24] 2412 	movx	a,@dptr
      001077 FC               [12] 2413 	mov	r4,a
      001078 EE               [12] 2414 	mov	a,r6
      001079 2B               [12] 2415 	add	a,r3
      00107A FE               [12] 2416 	mov	r6,a
      00107B ED               [12] 2417 	mov	a,r5
      00107C 3C               [12] 2418 	addc	a,r4
      00107D FD               [12] 2419 	mov	r5,a
      00107E 90 80 A1         [24] 2420 	mov	dptr,#___memcpy_PARM_2
      001081 74 7C            [12] 2421 	mov	a,#_handle_radio_request_payload_262144_95
      001083 F0               [24] 2422 	movx	@dptr,a
      001084 74 80            [12] 2423 	mov	a,#(_handle_radio_request_payload_262144_95 >> 8)
      001086 A3               [24] 2424 	inc	dptr
      001087 F0               [24] 2425 	movx	@dptr,a
      001088 E4               [12] 2426 	clr	a
      001089 A3               [24] 2427 	inc	dptr
      00108A F0               [24] 2428 	movx	@dptr,a
      00108B 90 80 A4         [24] 2429 	mov	dptr,#___memcpy_PARM_3
      00108E EE               [12] 2430 	mov	a,r6
      00108F F0               [24] 2431 	movx	@dptr,a
      001090 ED               [12] 2432 	mov	a,r5
      001091 A3               [24] 2433 	inc	dptr
      001092 F0               [24] 2434 	movx	@dptr,a
      001093 90 C6 80         [24] 2435 	mov	dptr,#_in1buf
      001096 75 F0 00         [24] 2436 	mov	b,#0x00
      001099 12 16 02         [24] 2437 	lcall	___memcpy
                                   2438 ;	src/radio.c:357: in1bc = pm_prefix_length + pm_payload_length;
      00109C 90 80 12         [24] 2439 	mov	dptr,#_pm_prefix_length
      00109F E0               [24] 2440 	movx	a,@dptr
      0010A0 FD               [12] 2441 	mov	r5,a
      0010A1 A3               [24] 2442 	inc	dptr
      0010A2 E0               [24] 2443 	movx	a,@dptr
      0010A3 90 80 19         [24] 2444 	mov	dptr,#_pm_payload_length
      0010A6 E0               [24] 2445 	movx	a,@dptr
      0010A7 2D               [12] 2446 	add	a,r5
      0010A8 90 C7 B7         [24] 2447 	mov	dptr,#0xc7b7
      0010AB F0               [24] 2448 	movx	@dptr,a
                                   2449 ;	src/radio.c:359: return;
      0010AC 22               [24] 2450 	ret
      0010AD                       2451 00133$:
                                   2452 ;	src/radio.c:364: in1bc = 1;
      0010AD 90 C7 B7         [24] 2453 	mov	dptr,#0xc7b7
      0010B0 74 01            [12] 2454 	mov	a,#0x01
      0010B2 F0               [24] 2455 	movx	@dptr,a
                                   2456 ;	src/radio.c:365: in1buf[0] = 0xFF;
      0010B3 90 C6 80         [24] 2457 	mov	dptr,#_in1buf
      0010B6 74 FF            [12] 2458 	mov	a,#0xff
      0010B8 F0               [24] 2459 	movx	@dptr,a
                                   2460 ;	src/radio.c:366: return;
      0010B9 22               [24] 2461 	ret
      0010BA                       2462 00189$:
                                   2463 ;	src/radio.c:370: else if(request == ENTER_SNIFFER_MODE)
      0010BA BF 05 02         [24] 2464 	cjne	r7,#0x05,00556$
      0010BD 80 03            [24] 2465 	sjmp	00557$
      0010BF                       2466 00556$:
      0010BF 02 11 75         [24] 2467 	ljmp	00186$
      0010C2                       2468 00557$:
                                   2469 ;	src/radio.c:372: radio_mode = sniffer;
      0010C2 90 80 11         [24] 2470 	mov	dptr,#_radio_mode
      0010C5 E4               [12] 2471 	clr	a
      0010C6 F0               [24] 2472 	movx	@dptr,a
                                   2473 ;	src/radio.c:375: if(data[0] > 5) data[0] = 5;
      0010C7 90 80 45         [24] 2474 	mov	dptr,#_handle_radio_request_PARM_2
      0010CA E0               [24] 2475 	movx	a,@dptr
      0010CB FC               [12] 2476 	mov	r4,a
      0010CC A3               [24] 2477 	inc	dptr
      0010CD E0               [24] 2478 	movx	a,@dptr
      0010CE FD               [12] 2479 	mov	r5,a
      0010CF A3               [24] 2480 	inc	dptr
      0010D0 E0               [24] 2481 	movx	a,@dptr
      0010D1 FE               [12] 2482 	mov	r6,a
      0010D2 8C 82            [24] 2483 	mov	dpl,r4
      0010D4 8D 83            [24] 2484 	mov	dph,r5
      0010D6 8E F0            [24] 2485 	mov	b,r6
      0010D8 12 16 D1         [24] 2486 	lcall	__gptrget
      0010DB 24 FA            [12] 2487 	add	a,#0xff - 0x05
      0010DD 50 0B            [24] 2488 	jnc	00135$
      0010DF 8C 82            [24] 2489 	mov	dpl,r4
      0010E1 8D 83            [24] 2490 	mov	dph,r5
      0010E3 8E F0            [24] 2491 	mov	b,r6
      0010E5 74 05            [12] 2492 	mov	a,#0x05
      0010E7 12 16 9E         [24] 2493 	lcall	__gptrput
      0010EA                       2494 00135$:
                                   2495 ;	src/radio.c:376: if(data[0] < 2) data[0] = 2;
      0010EA 8C 82            [24] 2496 	mov	dpl,r4
      0010EC 8D 83            [24] 2497 	mov	dph,r5
      0010EE 8E F0            [24] 2498 	mov	b,r6
      0010F0 12 16 D1         [24] 2499 	lcall	__gptrget
      0010F3 FB               [12] 2500 	mov	r3,a
      0010F4 BB 02 00         [24] 2501 	cjne	r3,#0x02,00559$
      0010F7                       2502 00559$:
      0010F7 50 0B            [24] 2503 	jnc	00137$
      0010F9 8C 82            [24] 2504 	mov	dpl,r4
      0010FB 8D 83            [24] 2505 	mov	dph,r5
      0010FD 8E F0            [24] 2506 	mov	b,r6
      0010FF 74 02            [12] 2507 	mov	a,#0x02
      001101 12 16 9E         [24] 2508 	lcall	__gptrput
      001104                       2509 00137$:
                                   2510 ;	src/radio.c:379: rfce = 0;
                                   2511 ;	assignBit
      001104 C2 90            [12] 2512 	clr	_rfce
                                   2513 ;	src/radio.c:382: configure_address(&data[1], data[0]);
      001106 74 01            [12] 2514 	mov	a,#0x01
      001108 2C               [12] 2515 	add	a,r4
      001109 F9               [12] 2516 	mov	r1,a
      00110A E4               [12] 2517 	clr	a
      00110B 3D               [12] 2518 	addc	a,r5
      00110C FA               [12] 2519 	mov	r2,a
      00110D 8E 03            [24] 2520 	mov	ar3,r6
      00110F 8C 82            [24] 2521 	mov	dpl,r4
      001111 8D 83            [24] 2522 	mov	dph,r5
      001113 8E F0            [24] 2523 	mov	b,r6
      001115 12 16 D1         [24] 2524 	lcall	__gptrget
      001118 90 80 28         [24] 2525 	mov	dptr,#_configure_address_PARM_2
      00111B F0               [24] 2526 	movx	@dptr,a
      00111C 89 82            [24] 2527 	mov	dpl,r1
      00111E 8A 83            [24] 2528 	mov	dph,r2
      001120 8B F0            [24] 2529 	mov	b,r3
      001122 12 07 7E         [24] 2530 	lcall	_configure_address
                                   2531 ;	src/radio.c:385: configure_mac(EN_DPL | EN_ACK_PAY, DPL_P0, ENAA_NONE);
      001125 90 80 2C         [24] 2532 	mov	dptr,#_configure_mac_PARM_2
      001128 74 01            [12] 2533 	mov	a,#0x01
      00112A F0               [24] 2534 	movx	@dptr,a
      00112B 90 80 2D         [24] 2535 	mov	dptr,#_configure_mac_PARM_3
      00112E E4               [12] 2536 	clr	a
      00112F F0               [24] 2537 	movx	@dptr,a
      001130 75 82 06         [24] 2538 	mov	dpl,#0x06
      001133 12 07 F7         [24] 2539 	lcall	_configure_mac
                                   2540 ;	src/radio.c:388: configure_phy(EN_CRC | CRC0 | PRIM_RX | PWR_UP, RATE_2M, 0);
      001136 90 80 2F         [24] 2541 	mov	dptr,#_configure_phy_PARM_2
      001139 74 08            [12] 2542 	mov	a,#0x08
      00113B F0               [24] 2543 	movx	@dptr,a
      00113C 90 80 30         [24] 2544 	mov	dptr,#_configure_phy_PARM_3
      00113F E4               [12] 2545 	clr	a
      001140 F0               [24] 2546 	movx	@dptr,a
      001141 75 82 0F         [24] 2547 	mov	dpl,#0x0f
      001144 12 08 24         [24] 2548 	lcall	_configure_phy
                                   2549 ;	src/radio.c:391: rfce = 1;
                                   2550 ;	assignBit
      001147 D2 90            [12] 2551 	setb	_rfce
                                   2552 ;	src/radio.c:394: flush_rx();
      001149 90 80 33         [24] 2553 	mov	dptr,#_spi_write_PARM_2
      00114C E4               [12] 2554 	clr	a
      00114D F0               [24] 2555 	movx	@dptr,a
      00114E A3               [24] 2556 	inc	dptr
      00114F F0               [24] 2557 	movx	@dptr,a
      001150 A3               [24] 2558 	inc	dptr
      001151 F0               [24] 2559 	movx	@dptr,a
      001152 90 80 36         [24] 2560 	mov	dptr,#_spi_write_PARM_3
      001155 F0               [24] 2561 	movx	@dptr,a
      001156 75 82 E2         [24] 2562 	mov	dpl,#0xe2
      001159 12 08 63         [24] 2563 	lcall	_spi_write
                                   2564 ;	src/radio.c:395: flush_tx();
      00115C 90 80 33         [24] 2565 	mov	dptr,#_spi_write_PARM_2
      00115F E4               [12] 2566 	clr	a
      001160 F0               [24] 2567 	movx	@dptr,a
      001161 A3               [24] 2568 	inc	dptr
      001162 F0               [24] 2569 	movx	@dptr,a
      001163 A3               [24] 2570 	inc	dptr
      001164 F0               [24] 2571 	movx	@dptr,a
      001165 90 80 36         [24] 2572 	mov	dptr,#_spi_write_PARM_3
      001168 F0               [24] 2573 	movx	@dptr,a
      001169 75 82 E1         [24] 2574 	mov	dpl,#0xe1
      00116C 12 08 63         [24] 2575 	lcall	_spi_write
                                   2576 ;	src/radio.c:396: in1bc = 0;
      00116F 90 C7 B7         [24] 2577 	mov	dptr,#0xc7b7
      001172 E4               [12] 2578 	clr	a
      001173 F0               [24] 2579 	movx	@dptr,a
      001174 22               [24] 2580 	ret
      001175                       2581 00186$:
                                   2582 ;	src/radio.c:400: else if(request == TRANSMIT_ACK_PAYLOAD)
      001175 BF 08 02         [24] 2583 	cjne	r7,#0x08,00561$
      001178 80 03            [24] 2584 	sjmp	00562$
      00117A                       2585 00561$:
      00117A 02 12 AC         [24] 2586 	ljmp	00183$
      00117D                       2587 00562$:
                                   2588 ;	src/radio.c:406: if(data[0] > 32) data[0] = 32;
      00117D 90 80 45         [24] 2589 	mov	dptr,#_handle_radio_request_PARM_2
      001180 E0               [24] 2590 	movx	a,@dptr
      001181 FC               [12] 2591 	mov	r4,a
      001182 A3               [24] 2592 	inc	dptr
      001183 E0               [24] 2593 	movx	a,@dptr
      001184 FD               [12] 2594 	mov	r5,a
      001185 A3               [24] 2595 	inc	dptr
      001186 E0               [24] 2596 	movx	a,@dptr
      001187 FE               [12] 2597 	mov	r6,a
      001188 8C 82            [24] 2598 	mov	dpl,r4
      00118A 8D 83            [24] 2599 	mov	dph,r5
      00118C 8E F0            [24] 2600 	mov	b,r6
      00118E 12 16 D1         [24] 2601 	lcall	__gptrget
      001191 24 DF            [12] 2602 	add	a,#0xff - 0x20
      001193 50 0B            [24] 2603 	jnc	00139$
      001195 8C 82            [24] 2604 	mov	dpl,r4
      001197 8D 83            [24] 2605 	mov	dph,r5
      001199 8E F0            [24] 2606 	mov	b,r6
      00119B 74 20            [12] 2607 	mov	a,#0x20
      00119D 12 16 9E         [24] 2608 	lcall	__gptrput
      0011A0                       2609 00139$:
                                   2610 ;	src/radio.c:407: if(data[0] < 1) data[0] = 1;
      0011A0 8C 82            [24] 2611 	mov	dpl,r4
      0011A2 8D 83            [24] 2612 	mov	dph,r5
      0011A4 8E F0            [24] 2613 	mov	b,r6
      0011A6 12 16 D1         [24] 2614 	lcall	__gptrget
      0011A9 FB               [12] 2615 	mov	r3,a
      0011AA BB 01 00         [24] 2616 	cjne	r3,#0x01,00564$
      0011AD                       2617 00564$:
      0011AD 50 0B            [24] 2618 	jnc	00141$
      0011AF 8C 82            [24] 2619 	mov	dpl,r4
      0011B1 8D 83            [24] 2620 	mov	dph,r5
      0011B3 8E F0            [24] 2621 	mov	b,r6
      0011B5 74 01            [12] 2622 	mov	a,#0x01
      0011B7 12 16 9E         [24] 2623 	lcall	__gptrput
      0011BA                       2624 00141$:
                                   2625 ;	src/radio.c:410: rfce = 0;
                                   2626 ;	assignBit
      0011BA C2 90            [12] 2627 	clr	_rfce
                                   2628 ;	src/radio.c:413: flush_tx();
      0011BC 90 80 33         [24] 2629 	mov	dptr,#_spi_write_PARM_2
      0011BF E4               [12] 2630 	clr	a
      0011C0 F0               [24] 2631 	movx	@dptr,a
      0011C1 A3               [24] 2632 	inc	dptr
      0011C2 F0               [24] 2633 	movx	@dptr,a
      0011C3 A3               [24] 2634 	inc	dptr
      0011C4 F0               [24] 2635 	movx	@dptr,a
      0011C5 90 80 36         [24] 2636 	mov	dptr,#_spi_write_PARM_3
      0011C8 F0               [24] 2637 	movx	@dptr,a
      0011C9 75 82 E1         [24] 2638 	mov	dpl,#0xe1
      0011CC C0 06            [24] 2639 	push	ar6
      0011CE C0 05            [24] 2640 	push	ar5
      0011D0 C0 04            [24] 2641 	push	ar4
      0011D2 12 08 63         [24] 2642 	lcall	_spi_write
      0011D5 D0 04            [24] 2643 	pop	ar4
      0011D7 D0 05            [24] 2644 	pop	ar5
      0011D9 D0 06            [24] 2645 	pop	ar6
                                   2646 ;	src/radio.c:414: flush_rx();
      0011DB 90 80 33         [24] 2647 	mov	dptr,#_spi_write_PARM_2
      0011DE E4               [12] 2648 	clr	a
      0011DF F0               [24] 2649 	movx	@dptr,a
      0011E0 A3               [24] 2650 	inc	dptr
      0011E1 F0               [24] 2651 	movx	@dptr,a
      0011E2 A3               [24] 2652 	inc	dptr
      0011E3 F0               [24] 2653 	movx	@dptr,a
      0011E4 90 80 36         [24] 2654 	mov	dptr,#_spi_write_PARM_3
      0011E7 F0               [24] 2655 	movx	@dptr,a
      0011E8 75 82 E2         [24] 2656 	mov	dpl,#0xe2
      0011EB C0 06            [24] 2657 	push	ar6
      0011ED C0 05            [24] 2658 	push	ar5
      0011EF C0 04            [24] 2659 	push	ar4
      0011F1 12 08 63         [24] 2660 	lcall	_spi_write
                                   2661 ;	src/radio.c:417: write_register_byte(STATUS, MAX_RT | TX_DS | RX_DR);
      0011F4 90 80 3D         [24] 2662 	mov	dptr,#_write_register_byte_PARM_2
      0011F7 74 70            [12] 2663 	mov	a,#0x70
      0011F9 F0               [24] 2664 	movx	@dptr,a
      0011FA 75 82 07         [24] 2665 	mov	dpl,#0x07
      0011FD 12 09 50         [24] 2666 	lcall	_write_register_byte
                                   2667 ;	src/radio.c:420: write_register_byte(EN_AA, ENAA_P0);
      001200 90 80 3D         [24] 2668 	mov	dptr,#_write_register_byte_PARM_2
      001203 74 01            [12] 2669 	mov	a,#0x01
      001205 F0               [24] 2670 	movx	@dptr,a
      001206 75 82 01         [24] 2671 	mov	dpl,#0x01
      001209 12 09 50         [24] 2672 	lcall	_write_register_byte
                                   2673 ;	src/radio.c:421: write_register_byte(FEATURE, EN_DPL | EN_ACK_PAY);
      00120C 90 80 3D         [24] 2674 	mov	dptr,#_write_register_byte_PARM_2
      00120F 74 06            [12] 2675 	mov	a,#0x06
      001211 F0               [24] 2676 	movx	@dptr,a
      001212 75 82 1D         [24] 2677 	mov	dpl,#0x1d
      001215 12 09 50         [24] 2678 	lcall	_write_register_byte
      001218 D0 04            [24] 2679 	pop	ar4
      00121A D0 05            [24] 2680 	pop	ar5
      00121C D0 06            [24] 2681 	pop	ar6
                                   2682 ;	src/radio.c:424: spi_write(W_ACK_PAYLOAD, &data[1], data[0]);
      00121E 74 01            [12] 2683 	mov	a,#0x01
      001220 2C               [12] 2684 	add	a,r4
      001221 F9               [12] 2685 	mov	r1,a
      001222 E4               [12] 2686 	clr	a
      001223 3D               [12] 2687 	addc	a,r5
      001224 FA               [12] 2688 	mov	r2,a
      001225 8E 03            [24] 2689 	mov	ar3,r6
      001227 8C 82            [24] 2690 	mov	dpl,r4
      001229 8D 83            [24] 2691 	mov	dph,r5
      00122B 8E F0            [24] 2692 	mov	b,r6
      00122D 12 16 D1         [24] 2693 	lcall	__gptrget
      001230 FC               [12] 2694 	mov	r4,a
      001231 90 80 33         [24] 2695 	mov	dptr,#_spi_write_PARM_2
      001234 E9               [12] 2696 	mov	a,r1
      001235 F0               [24] 2697 	movx	@dptr,a
      001236 EA               [12] 2698 	mov	a,r2
      001237 A3               [24] 2699 	inc	dptr
      001238 F0               [24] 2700 	movx	@dptr,a
      001239 EB               [12] 2701 	mov	a,r3
      00123A A3               [24] 2702 	inc	dptr
      00123B F0               [24] 2703 	movx	@dptr,a
      00123C 90 80 36         [24] 2704 	mov	dptr,#_spi_write_PARM_3
      00123F EC               [12] 2705 	mov	a,r4
      001240 F0               [24] 2706 	movx	@dptr,a
      001241 75 82 A8         [24] 2707 	mov	dpl,#0xa8
      001244 12 08 63         [24] 2708 	lcall	_spi_write
                                   2709 ;	src/radio.c:427: rfce = 1;
                                   2710 ;	assignBit
      001247 D2 90            [12] 2711 	setb	_rfce
                                   2712 ;	src/radio.c:431: in1buf[0] = 0;
      001249 90 C6 80         [24] 2713 	mov	dptr,#_in1buf
      00124C E4               [12] 2714 	clr	a
      00124D F0               [24] 2715 	movx	@dptr,a
                                   2716 ;	src/radio.c:432: while(elapsed < 500)
      00124E 7D 00            [12] 2717 	mov	r5,#0x00
      001250 7E 00            [12] 2718 	mov	r6,#0x00
      001252                       2719 00144$:
      001252 8D 03            [24] 2720 	mov	ar3,r5
      001254 8E 04            [24] 2721 	mov	ar4,r6
      001256 C3               [12] 2722 	clr	c
      001257 EB               [12] 2723 	mov	a,r3
      001258 94 F4            [12] 2724 	subb	a,#0xf4
      00125A EC               [12] 2725 	mov	a,r4
      00125B 94 01            [12] 2726 	subb	a,#0x01
      00125D 50 3B            [24] 2727 	jnc	00146$
                                   2728 ;	src/radio.c:434: status = read_register_byte(STATUS);
      00125F 75 82 07         [24] 2729 	mov	dpl,#0x07
      001262 C0 06            [24] 2730 	push	ar6
      001264 C0 05            [24] 2731 	push	ar5
      001266 12 09 71         [24] 2732 	lcall	_read_register_byte
      001269 AC 82            [24] 2733 	mov	r4,dpl
      00126B D0 05            [24] 2734 	pop	ar5
      00126D D0 06            [24] 2735 	pop	ar6
                                   2736 ;	src/radio.c:435: if((status & RX_DR) == RX_DR)
      00126F 53 04 40         [24] 2737 	anl	ar4,#0x40
      001272 7B 00            [12] 2738 	mov	r3,#0x00
      001274 BC 40 0B         [24] 2739 	cjne	r4,#0x40,00285$
      001277 BB 00 08         [24] 2740 	cjne	r3,#0x00,00285$
                                   2741 ;	src/radio.c:437: in1buf[0] = 1;
      00127A 90 C6 80         [24] 2742 	mov	dptr,#_in1buf
      00127D 74 01            [12] 2743 	mov	a,#0x01
      00127F F0               [24] 2744 	movx	@dptr,a
                                   2745 ;	src/radio.c:438: break;
                                   2746 ;	src/nRF24LU1P.h:35: inline void delay_us(uint16_t us) { do nop_us(); while(--us); }
      001280 80 18            [24] 2747 	sjmp	00146$
      001282                       2748 00285$:
      001282 7B E8            [12] 2749 	mov	r3,#0xe8
      001284 7C 03            [12] 2750 	mov	r4,#0x03
      001286                       2751 00212$:
      001286 00               [12] 2752 	nop 
      001287 00               [12] 2753 	nop 
      001288 00               [12] 2754 	nop 
      001289 00               [12] 2755 	nop 
      00128A 1B               [12] 2756 	dec	r3
      00128B BB FF 01         [24] 2757 	cjne	r3,#0xff,00569$
      00128E 1C               [12] 2758 	dec	r4
      00128F                       2759 00569$:
      00128F EB               [12] 2760 	mov	a,r3
      001290 4C               [12] 2761 	orl	a,r4
      001291 70 F3            [24] 2762 	jnz	00212$
                                   2763 ;	src/radio.c:442: elapsed++;
      001293 0D               [12] 2764 	inc	r5
      001294 BD 00 BB         [24] 2765 	cjne	r5,#0x00,00144$
      001297 0E               [12] 2766 	inc	r6
      001298 80 B8            [24] 2767 	sjmp	00144$
      00129A                       2768 00146$:
                                   2769 ;	src/radio.c:446: write_register_byte(EN_AA, ENAA_NONE);
      00129A 90 80 3D         [24] 2770 	mov	dptr,#_write_register_byte_PARM_2
      00129D E4               [12] 2771 	clr	a
      00129E F0               [24] 2772 	movx	@dptr,a
      00129F 75 82 01         [24] 2773 	mov	dpl,#0x01
      0012A2 12 09 50         [24] 2774 	lcall	_write_register_byte
                                   2775 ;	src/radio.c:448: in1bc = 1;
      0012A5 90 C7 B7         [24] 2776 	mov	dptr,#0xc7b7
      0012A8 74 01            [12] 2777 	mov	a,#0x01
      0012AA F0               [24] 2778 	movx	@dptr,a
      0012AB 22               [24] 2779 	ret
      0012AC                       2780 00183$:
                                   2781 ;	src/radio.c:452: else if(request == TRANSMIT_PAYLOAD)
      0012AC BF 04 02         [24] 2782 	cjne	r7,#0x04,00572$
      0012AF 80 03            [24] 2783 	sjmp	00573$
      0012B1                       2784 00572$:
      0012B1 02 14 40         [24] 2785 	ljmp	00180$
      0012B4                       2786 00573$:
                                   2787 ;	src/radio.c:455: if(data[0] > 32) data[0] = 32;
      0012B4 90 80 45         [24] 2788 	mov	dptr,#_handle_radio_request_PARM_2
      0012B7 E0               [24] 2789 	movx	a,@dptr
      0012B8 FC               [12] 2790 	mov	r4,a
      0012B9 A3               [24] 2791 	inc	dptr
      0012BA E0               [24] 2792 	movx	a,@dptr
      0012BB FD               [12] 2793 	mov	r5,a
      0012BC A3               [24] 2794 	inc	dptr
      0012BD E0               [24] 2795 	movx	a,@dptr
      0012BE FE               [12] 2796 	mov	r6,a
      0012BF 8C 82            [24] 2797 	mov	dpl,r4
      0012C1 8D 83            [24] 2798 	mov	dph,r5
      0012C3 8E F0            [24] 2799 	mov	b,r6
      0012C5 12 16 D1         [24] 2800 	lcall	__gptrget
      0012C8 24 DF            [12] 2801 	add	a,#0xff - 0x20
      0012CA 50 0B            [24] 2802 	jnc	00148$
      0012CC 8C 82            [24] 2803 	mov	dpl,r4
      0012CE 8D 83            [24] 2804 	mov	dph,r5
      0012D0 8E F0            [24] 2805 	mov	b,r6
      0012D2 74 20            [12] 2806 	mov	a,#0x20
      0012D4 12 16 9E         [24] 2807 	lcall	__gptrput
      0012D7                       2808 00148$:
                                   2809 ;	src/radio.c:456: if(data[0] < 1) data[0] = 1;
      0012D7 8C 82            [24] 2810 	mov	dpl,r4
      0012D9 8D 83            [24] 2811 	mov	dph,r5
      0012DB 8E F0            [24] 2812 	mov	b,r6
      0012DD 12 16 D1         [24] 2813 	lcall	__gptrget
      0012E0 FB               [12] 2814 	mov	r3,a
      0012E1 BB 01 00         [24] 2815 	cjne	r3,#0x01,00575$
      0012E4                       2816 00575$:
      0012E4 50 0B            [24] 2817 	jnc	00150$
      0012E6 8C 82            [24] 2818 	mov	dpl,r4
      0012E8 8D 83            [24] 2819 	mov	dph,r5
      0012EA 8E F0            [24] 2820 	mov	b,r6
      0012EC 74 01            [12] 2821 	mov	a,#0x01
      0012EE 12 16 9E         [24] 2822 	lcall	__gptrput
      0012F1                       2823 00150$:
                                   2824 ;	src/radio.c:459: rfce = 0;
                                   2825 ;	assignBit
      0012F1 C2 90            [12] 2826 	clr	_rfce
                                   2827 ;	src/radio.c:463: write_register_byte(SETUP_RETR, (1 << data[1]) | data[2]);
      0012F3 74 01            [12] 2828 	mov	a,#0x01
      0012F5 2C               [12] 2829 	add	a,r4
      0012F6 F9               [12] 2830 	mov	r1,a
      0012F7 E4               [12] 2831 	clr	a
      0012F8 3D               [12] 2832 	addc	a,r5
      0012F9 FA               [12] 2833 	mov	r2,a
      0012FA 8E 03            [24] 2834 	mov	ar3,r6
      0012FC 89 82            [24] 2835 	mov	dpl,r1
      0012FE 8A 83            [24] 2836 	mov	dph,r2
      001300 8B F0            [24] 2837 	mov	b,r3
      001302 12 16 D1         [24] 2838 	lcall	__gptrget
      001305 F9               [12] 2839 	mov	r1,a
      001306 89 F0            [24] 2840 	mov	b,r1
      001308 05 F0            [12] 2841 	inc	b
      00130A 74 01            [12] 2842 	mov	a,#0x01
      00130C 80 02            [24] 2843 	sjmp	00579$
      00130E                       2844 00577$:
      00130E 25 E0            [12] 2845 	add	a,acc
      001310                       2846 00579$:
      001310 D5 F0 FB         [24] 2847 	djnz	b,00577$
      001313 F9               [12] 2848 	mov	r1,a
      001314 74 02            [12] 2849 	mov	a,#0x02
      001316 2C               [12] 2850 	add	a,r4
      001317 F8               [12] 2851 	mov	r0,a
      001318 E4               [12] 2852 	clr	a
      001319 3D               [12] 2853 	addc	a,r5
      00131A FA               [12] 2854 	mov	r2,a
      00131B 8E 03            [24] 2855 	mov	ar3,r6
      00131D 88 82            [24] 2856 	mov	dpl,r0
      00131F 8A 83            [24] 2857 	mov	dph,r2
      001321 8B F0            [24] 2858 	mov	b,r3
      001323 12 16 D1         [24] 2859 	lcall	__gptrget
      001326 90 80 3D         [24] 2860 	mov	dptr,#_write_register_byte_PARM_2
      001329 49               [12] 2861 	orl	a,r1
      00132A F0               [24] 2862 	movx	@dptr,a
      00132B 75 82 04         [24] 2863 	mov	dpl,#0x04
      00132E C0 06            [24] 2864 	push	ar6
      001330 C0 05            [24] 2865 	push	ar5
      001332 C0 04            [24] 2866 	push	ar4
      001334 12 09 50         [24] 2867 	lcall	_write_register_byte
      001337 D0 04            [24] 2868 	pop	ar4
      001339 D0 05            [24] 2869 	pop	ar5
      00133B D0 06            [24] 2870 	pop	ar6
                                   2871 ;	src/radio.c:466: flush_tx();
      00133D 90 80 33         [24] 2872 	mov	dptr,#_spi_write_PARM_2
      001340 E4               [12] 2873 	clr	a
      001341 F0               [24] 2874 	movx	@dptr,a
      001342 A3               [24] 2875 	inc	dptr
      001343 F0               [24] 2876 	movx	@dptr,a
      001344 A3               [24] 2877 	inc	dptr
      001345 F0               [24] 2878 	movx	@dptr,a
      001346 90 80 36         [24] 2879 	mov	dptr,#_spi_write_PARM_3
      001349 F0               [24] 2880 	movx	@dptr,a
      00134A 75 82 E1         [24] 2881 	mov	dpl,#0xe1
      00134D C0 06            [24] 2882 	push	ar6
      00134F C0 05            [24] 2883 	push	ar5
      001351 C0 04            [24] 2884 	push	ar4
      001353 12 08 63         [24] 2885 	lcall	_spi_write
      001356 D0 04            [24] 2886 	pop	ar4
      001358 D0 05            [24] 2887 	pop	ar5
      00135A D0 06            [24] 2888 	pop	ar6
                                   2889 ;	src/radio.c:467: flush_rx();
      00135C 90 80 33         [24] 2890 	mov	dptr,#_spi_write_PARM_2
      00135F E4               [12] 2891 	clr	a
      001360 F0               [24] 2892 	movx	@dptr,a
      001361 A3               [24] 2893 	inc	dptr
      001362 F0               [24] 2894 	movx	@dptr,a
      001363 A3               [24] 2895 	inc	dptr
      001364 F0               [24] 2896 	movx	@dptr,a
      001365 90 80 36         [24] 2897 	mov	dptr,#_spi_write_PARM_3
      001368 F0               [24] 2898 	movx	@dptr,a
      001369 75 82 E2         [24] 2899 	mov	dpl,#0xe2
      00136C C0 06            [24] 2900 	push	ar6
      00136E C0 05            [24] 2901 	push	ar5
      001370 C0 04            [24] 2902 	push	ar4
      001372 12 08 63         [24] 2903 	lcall	_spi_write
                                   2904 ;	src/radio.c:470: write_register_byte(STATUS, MAX_RT | TX_DS | RX_DR);
      001375 90 80 3D         [24] 2905 	mov	dptr,#_write_register_byte_PARM_2
      001378 74 70            [12] 2906 	mov	a,#0x70
      00137A F0               [24] 2907 	movx	@dptr,a
      00137B 75 82 07         [24] 2908 	mov	dpl,#0x07
      00137E 12 09 50         [24] 2909 	lcall	_write_register_byte
                                   2910 ;	src/radio.c:473: write_register_byte(CONFIG, read_register_byte(CONFIG) & ~PRIM_RX);
      001381 75 82 00         [24] 2911 	mov	dpl,#0x00
      001384 12 09 71         [24] 2912 	lcall	_read_register_byte
      001387 E5 82            [12] 2913 	mov	a,dpl
      001389 90 80 3D         [24] 2914 	mov	dptr,#_write_register_byte_PARM_2
      00138C 54 FE            [12] 2915 	anl	a,#0xfe
      00138E F0               [24] 2916 	movx	@dptr,a
      00138F 75 82 00         [24] 2917 	mov	dpl,#0x00
      001392 12 09 50         [24] 2918 	lcall	_write_register_byte
                                   2919 ;	src/radio.c:476: write_register_byte(EN_AA, ENAA_P0);
      001395 90 80 3D         [24] 2920 	mov	dptr,#_write_register_byte_PARM_2
      001398 74 01            [12] 2921 	mov	a,#0x01
      00139A F0               [24] 2922 	movx	@dptr,a
      00139B 75 82 01         [24] 2923 	mov	dpl,#0x01
      00139E 12 09 50         [24] 2924 	lcall	_write_register_byte
      0013A1 D0 04            [24] 2925 	pop	ar4
      0013A3 D0 05            [24] 2926 	pop	ar5
      0013A5 D0 06            [24] 2927 	pop	ar6
                                   2928 ;	src/radio.c:479: spi_write(W_TX_PAYLOAD, &data[3], data[0]);
      0013A7 74 03            [12] 2929 	mov	a,#0x03
      0013A9 2C               [12] 2930 	add	a,r4
      0013AA F9               [12] 2931 	mov	r1,a
      0013AB E4               [12] 2932 	clr	a
      0013AC 3D               [12] 2933 	addc	a,r5
      0013AD FA               [12] 2934 	mov	r2,a
      0013AE 8E 03            [24] 2935 	mov	ar3,r6
      0013B0 8C 82            [24] 2936 	mov	dpl,r4
      0013B2 8D 83            [24] 2937 	mov	dph,r5
      0013B4 8E F0            [24] 2938 	mov	b,r6
      0013B6 12 16 D1         [24] 2939 	lcall	__gptrget
      0013B9 FC               [12] 2940 	mov	r4,a
      0013BA 90 80 33         [24] 2941 	mov	dptr,#_spi_write_PARM_2
      0013BD E9               [12] 2942 	mov	a,r1
      0013BE F0               [24] 2943 	movx	@dptr,a
      0013BF EA               [12] 2944 	mov	a,r2
      0013C0 A3               [24] 2945 	inc	dptr
      0013C1 F0               [24] 2946 	movx	@dptr,a
      0013C2 EB               [12] 2947 	mov	a,r3
      0013C3 A3               [24] 2948 	inc	dptr
      0013C4 F0               [24] 2949 	movx	@dptr,a
      0013C5 90 80 36         [24] 2950 	mov	dptr,#_spi_write_PARM_3
      0013C8 EC               [12] 2951 	mov	a,r4
      0013C9 F0               [24] 2952 	movx	@dptr,a
      0013CA 75 82 A0         [24] 2953 	mov	dpl,#0xa0
      0013CD 12 08 63         [24] 2954 	lcall	_spi_write
                                   2955 ;	src/radio.c:482: rfce = 1;
                                   2956 ;	assignBit
      0013D0 D2 90            [12] 2957 	setb	_rfce
                                   2958 ;	src/nRF24LU1P.h:35: inline void delay_us(uint16_t us) { do nop_us(); while(--us); }
      0013D2 7D 0A            [12] 2959 	mov	r5,#0x0a
      0013D4 7E 00            [12] 2960 	mov	r6,#0x00
      0013D6                       2961 00216$:
      0013D6 00               [12] 2962 	nop 
      0013D7 00               [12] 2963 	nop 
      0013D8 00               [12] 2964 	nop 
      0013D9 00               [12] 2965 	nop 
      0013DA 1D               [12] 2966 	dec	r5
      0013DB BD FF 01         [24] 2967 	cjne	r5,#0xff,00580$
      0013DE 1E               [12] 2968 	dec	r6
      0013DF                       2969 00580$:
      0013DF ED               [12] 2970 	mov	a,r5
      0013E0 4E               [12] 2971 	orl	a,r6
      0013E1 70 F3            [24] 2972 	jnz	00216$
                                   2973 ;	src/radio.c:484: rfce = 0;
                                   2974 ;	assignBit
      0013E3 C2 90            [12] 2975 	clr	_rfce
                                   2976 ;	src/radio.c:487: while(true)
      0013E5                       2977 00159$:
                                   2978 ;	src/radio.c:490: rfcsn = 0;
                                   2979 ;	assignBit
      0013E5 C2 91            [12] 2980 	clr	_rfcsn
                                   2981 ;	src/radio.c:491: RFDAT = _NOP;
      0013E7 75 E5 FF         [24] 2982 	mov	_RFDAT,#0xff
                                   2983 ;	src/radio.c:492: RFRDY = 0;
                                   2984 ;	assignBit
      0013EA C2 C0            [12] 2985 	clr	_RFRDY
                                   2986 ;	src/radio.c:493: while(!RFRDY);
      0013EC                       2987 00151$:
      0013EC 30 C0 FD         [24] 2988 	jnb	_RFRDY,00151$
                                   2989 ;	src/radio.c:494: rfcsn = 1;
                                   2990 ;	assignBit
      0013EF D2 91            [12] 2991 	setb	_rfcsn
                                   2992 ;	src/radio.c:497: if((RFDAT & 0x10) == 0x10)
      0013F1 AD E5            [24] 2993 	mov	r5,_RFDAT
      0013F3 53 05 10         [24] 2994 	anl	ar5,#0x10
      0013F6 7E 00            [12] 2995 	mov	r6,#0x00
      0013F8 BD 10 0A         [24] 2996 	cjne	r5,#0x10,00155$
      0013FB BE 00 07         [24] 2997 	cjne	r6,#0x00,00155$
                                   2998 ;	src/radio.c:499: in1buf[0] = 0;
      0013FE 90 C6 80         [24] 2999 	mov	dptr,#_in1buf
      001401 E4               [12] 3000 	clr	a
      001402 F0               [24] 3001 	movx	@dptr,a
                                   3002 ;	src/radio.c:500: break;
      001403 80 13            [24] 3003 	sjmp	00160$
      001405                       3004 00155$:
                                   3005 ;	src/radio.c:504: if((RFDAT & 0x20) == 0x20)
      001405 AD E5            [24] 3006 	mov	r5,_RFDAT
      001407 53 05 20         [24] 3007 	anl	ar5,#0x20
      00140A 7E 00            [12] 3008 	mov	r6,#0x00
      00140C BD 20 D6         [24] 3009 	cjne	r5,#0x20,00159$
      00140F BE 00 D3         [24] 3010 	cjne	r6,#0x00,00159$
                                   3011 ;	src/radio.c:506: in1buf[0] = 1;
      001412 90 C6 80         [24] 3012 	mov	dptr,#_in1buf
      001415 74 01            [12] 3013 	mov	a,#0x01
      001417 F0               [24] 3014 	movx	@dptr,a
                                   3015 ;	src/radio.c:507: break;
      001418                       3016 00160$:
                                   3017 ;	src/radio.c:512: write_register_byte(EN_AA, ENAA_NONE);
      001418 90 80 3D         [24] 3018 	mov	dptr,#_write_register_byte_PARM_2
      00141B E4               [12] 3019 	clr	a
      00141C F0               [24] 3020 	movx	@dptr,a
      00141D 75 82 01         [24] 3021 	mov	dpl,#0x01
      001420 12 09 50         [24] 3022 	lcall	_write_register_byte
                                   3023 ;	src/radio.c:515: write_register_byte(CONFIG, read_register_byte(CONFIG) | PRIM_RX);
      001423 75 82 00         [24] 3024 	mov	dpl,#0x00
      001426 12 09 71         [24] 3025 	lcall	_read_register_byte
      001429 E5 82            [12] 3026 	mov	a,dpl
      00142B 90 80 3D         [24] 3027 	mov	dptr,#_write_register_byte_PARM_2
      00142E 44 01            [12] 3028 	orl	a,#0x01
      001430 F0               [24] 3029 	movx	@dptr,a
      001431 75 82 00         [24] 3030 	mov	dpl,#0x00
      001434 12 09 50         [24] 3031 	lcall	_write_register_byte
                                   3032 ;	src/radio.c:518: rfce = 1;
                                   3033 ;	assignBit
      001437 D2 90            [12] 3034 	setb	_rfce
                                   3035 ;	src/radio.c:519: in1bc = 1;
      001439 90 C7 B7         [24] 3036 	mov	dptr,#0xc7b7
      00143C 74 01            [12] 3037 	mov	a,#0x01
      00143E F0               [24] 3038 	movx	@dptr,a
      00143F 22               [24] 3039 	ret
      001440                       3040 00180$:
                                   3041 ;	src/radio.c:523: else if(request == TRANSMIT_PAYLOAD_GENERIC)
      001440 BF 0C 02         [24] 3042 	cjne	r7,#0x0c,00587$
      001443 80 01            [24] 3043 	sjmp	00588$
      001445                       3044 00587$:
      001445 22               [24] 3045 	ret
      001446                       3046 00588$:
                                   3047 ;	src/radio.c:525: uint8_t address_start = data[0] + data[1] + 2;
      001446 90 80 45         [24] 3048 	mov	dptr,#_handle_radio_request_PARM_2
      001449 E0               [24] 3049 	movx	a,@dptr
      00144A FD               [12] 3050 	mov	r5,a
      00144B A3               [24] 3051 	inc	dptr
      00144C E0               [24] 3052 	movx	a,@dptr
      00144D FE               [12] 3053 	mov	r6,a
      00144E A3               [24] 3054 	inc	dptr
      00144F E0               [24] 3055 	movx	a,@dptr
      001450 FF               [12] 3056 	mov	r7,a
      001451 8D 82            [24] 3057 	mov	dpl,r5
      001453 8E 83            [24] 3058 	mov	dph,r6
      001455 8F F0            [24] 3059 	mov	b,r7
      001457 12 16 D1         [24] 3060 	lcall	__gptrget
      00145A FC               [12] 3061 	mov	r4,a
      00145B 74 01            [12] 3062 	mov	a,#0x01
      00145D 2D               [12] 3063 	add	a,r5
      00145E F5 2F            [12] 3064 	mov	_handle_radio_request_sloc1_1_0,a
      001460 E4               [12] 3065 	clr	a
      001461 3E               [12] 3066 	addc	a,r6
      001462 F5 30            [12] 3067 	mov	(_handle_radio_request_sloc1_1_0 + 1),a
      001464 8F 31            [24] 3068 	mov	(_handle_radio_request_sloc1_1_0 + 2),r7
      001466 85 2F 82         [24] 3069 	mov	dpl,_handle_radio_request_sloc1_1_0
      001469 85 30 83         [24] 3070 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      00146C 85 31 F0         [24] 3071 	mov	b,(_handle_radio_request_sloc1_1_0 + 2)
      00146F 12 16 D1         [24] 3072 	lcall	__gptrget
      001472 2C               [12] 3073 	add	a,r4
      001473 F8               [12] 3074 	mov	r0,a
      001474 08               [12] 3075 	inc	r0
      001475 08               [12] 3076 	inc	r0
                                   3077 ;	src/radio.c:528: if(data[0] > 32) data[0] = 32;
      001476 EC               [12] 3078 	mov	a,r4
      001477 24 DF            [12] 3079 	add	a,#0xff - 0x20
      001479 50 0B            [24] 3080 	jnc	00162$
      00147B 8D 82            [24] 3081 	mov	dpl,r5
      00147D 8E 83            [24] 3082 	mov	dph,r6
      00147F 8F F0            [24] 3083 	mov	b,r7
      001481 74 20            [12] 3084 	mov	a,#0x20
      001483 12 16 9E         [24] 3085 	lcall	__gptrput
      001486                       3086 00162$:
                                   3087 ;	src/radio.c:529: if(data[0] < 1) data[0] = 1;
      001486 8D 82            [24] 3088 	mov	dpl,r5
      001488 8E 83            [24] 3089 	mov	dph,r6
      00148A 8F F0            [24] 3090 	mov	b,r7
      00148C 12 16 D1         [24] 3091 	lcall	__gptrget
      00148F FC               [12] 3092 	mov	r4,a
      001490 BC 01 00         [24] 3093 	cjne	r4,#0x01,00590$
      001493                       3094 00590$:
      001493 50 0B            [24] 3095 	jnc	00164$
      001495 8D 82            [24] 3096 	mov	dpl,r5
      001497 8E 83            [24] 3097 	mov	dph,r6
      001499 8F F0            [24] 3098 	mov	b,r7
      00149B 74 01            [12] 3099 	mov	a,#0x01
      00149D 12 16 9E         [24] 3100 	lcall	__gptrput
      0014A0                       3101 00164$:
                                   3102 ;	src/radio.c:532: if(data[1] > 5) data[1] = 5;
      0014A0 85 2F 82         [24] 3103 	mov	dpl,_handle_radio_request_sloc1_1_0
      0014A3 85 30 83         [24] 3104 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      0014A6 85 31 F0         [24] 3105 	mov	b,(_handle_radio_request_sloc1_1_0 + 2)
      0014A9 12 16 D1         [24] 3106 	lcall	__gptrget
      0014AC 24 FA            [12] 3107 	add	a,#0xff - 0x05
      0014AE 50 0E            [24] 3108 	jnc	00166$
      0014B0 85 2F 82         [24] 3109 	mov	dpl,_handle_radio_request_sloc1_1_0
      0014B3 85 30 83         [24] 3110 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      0014B6 85 31 F0         [24] 3111 	mov	b,(_handle_radio_request_sloc1_1_0 + 2)
      0014B9 74 05            [12] 3112 	mov	a,#0x05
      0014BB 12 16 9E         [24] 3113 	lcall	__gptrput
      0014BE                       3114 00166$:
                                   3115 ;	src/radio.c:533: if(data[1] < 1) data[1] = 1;
      0014BE 85 2F 82         [24] 3116 	mov	dpl,_handle_radio_request_sloc1_1_0
      0014C1 85 30 83         [24] 3117 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      0014C4 85 31 F0         [24] 3118 	mov	b,(_handle_radio_request_sloc1_1_0 + 2)
      0014C7 12 16 D1         [24] 3119 	lcall	__gptrget
      0014CA FC               [12] 3120 	mov	r4,a
      0014CB BC 01 00         [24] 3121 	cjne	r4,#0x01,00593$
      0014CE                       3122 00593$:
      0014CE 50 0E            [24] 3123 	jnc	00168$
      0014D0 85 2F 82         [24] 3124 	mov	dpl,_handle_radio_request_sloc1_1_0
      0014D3 85 30 83         [24] 3125 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      0014D6 85 31 F0         [24] 3126 	mov	b,(_handle_radio_request_sloc1_1_0 + 2)
      0014D9 74 01            [12] 3127 	mov	a,#0x01
      0014DB 12 16 9E         [24] 3128 	lcall	__gptrput
      0014DE                       3129 00168$:
                                   3130 ;	src/radio.c:536: rfce = 0;
                                   3131 ;	assignBit
      0014DE C2 90            [12] 3132 	clr	_rfce
                                   3133 ;	src/radio.c:539: flush_tx();
      0014E0 90 80 33         [24] 3134 	mov	dptr,#_spi_write_PARM_2
      0014E3 E4               [12] 3135 	clr	a
      0014E4 F0               [24] 3136 	movx	@dptr,a
      0014E5 A3               [24] 3137 	inc	dptr
      0014E6 F0               [24] 3138 	movx	@dptr,a
      0014E7 A3               [24] 3139 	inc	dptr
      0014E8 F0               [24] 3140 	movx	@dptr,a
      0014E9 90 80 36         [24] 3141 	mov	dptr,#_spi_write_PARM_3
      0014EC F0               [24] 3142 	movx	@dptr,a
      0014ED 75 82 E1         [24] 3143 	mov	dpl,#0xe1
      0014F0 C0 07            [24] 3144 	push	ar7
      0014F2 C0 06            [24] 3145 	push	ar6
      0014F4 C0 05            [24] 3146 	push	ar5
      0014F6 C0 00            [24] 3147 	push	ar0
      0014F8 12 08 63         [24] 3148 	lcall	_spi_write
      0014FB D0 00            [24] 3149 	pop	ar0
      0014FD D0 05            [24] 3150 	pop	ar5
      0014FF D0 06            [24] 3151 	pop	ar6
      001501 D0 07            [24] 3152 	pop	ar7
                                   3153 ;	src/radio.c:540: flush_rx();
      001503 90 80 33         [24] 3154 	mov	dptr,#_spi_write_PARM_2
      001506 E4               [12] 3155 	clr	a
      001507 F0               [24] 3156 	movx	@dptr,a
      001508 A3               [24] 3157 	inc	dptr
      001509 F0               [24] 3158 	movx	@dptr,a
      00150A A3               [24] 3159 	inc	dptr
      00150B F0               [24] 3160 	movx	@dptr,a
      00150C 90 80 36         [24] 3161 	mov	dptr,#_spi_write_PARM_3
      00150F F0               [24] 3162 	movx	@dptr,a
      001510 75 82 E2         [24] 3163 	mov	dpl,#0xe2
      001513 C0 07            [24] 3164 	push	ar7
      001515 C0 06            [24] 3165 	push	ar6
      001517 C0 05            [24] 3166 	push	ar5
      001519 C0 00            [24] 3167 	push	ar0
      00151B 12 08 63         [24] 3168 	lcall	_spi_write
                                   3169 ;	src/radio.c:543: write_register_byte(STATUS, MAX_RT | TX_DS | RX_DR);
      00151E 90 80 3D         [24] 3170 	mov	dptr,#_write_register_byte_PARM_2
      001521 74 70            [12] 3171 	mov	a,#0x70
      001523 F0               [24] 3172 	movx	@dptr,a
      001524 75 82 07         [24] 3173 	mov	dpl,#0x07
      001527 12 09 50         [24] 3174 	lcall	_write_register_byte
                                   3175 ;	src/radio.c:546: write_register_byte(CONFIG, read_register_byte(CONFIG) & ~PRIM_RX);
      00152A 75 82 00         [24] 3176 	mov	dpl,#0x00
      00152D 12 09 71         [24] 3177 	lcall	_read_register_byte
      001530 E5 82            [12] 3178 	mov	a,dpl
      001532 90 80 3D         [24] 3179 	mov	dptr,#_write_register_byte_PARM_2
      001535 54 FE            [12] 3180 	anl	a,#0xfe
      001537 F0               [24] 3181 	movx	@dptr,a
      001538 75 82 00         [24] 3182 	mov	dpl,#0x00
      00153B 12 09 50         [24] 3183 	lcall	_write_register_byte
      00153E D0 00            [24] 3184 	pop	ar0
      001540 D0 05            [24] 3185 	pop	ar5
      001542 D0 06            [24] 3186 	pop	ar6
      001544 D0 07            [24] 3187 	pop	ar7
                                   3188 ;	src/radio.c:549: configure_address(&data[address_start], data[1]);
      001546 E8               [12] 3189 	mov	a,r0
      001547 2D               [12] 3190 	add	a,r5
      001548 F8               [12] 3191 	mov	r0,a
      001549 E4               [12] 3192 	clr	a
      00154A 3E               [12] 3193 	addc	a,r6
      00154B FB               [12] 3194 	mov	r3,a
      00154C 8F 04            [24] 3195 	mov	ar4,r7
      00154E 85 2F 82         [24] 3196 	mov	dpl,_handle_radio_request_sloc1_1_0
      001551 85 30 83         [24] 3197 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      001554 85 31 F0         [24] 3198 	mov	b,(_handle_radio_request_sloc1_1_0 + 2)
      001557 12 16 D1         [24] 3199 	lcall	__gptrget
      00155A 90 80 28         [24] 3200 	mov	dptr,#_configure_address_PARM_2
      00155D F0               [24] 3201 	movx	@dptr,a
      00155E 88 82            [24] 3202 	mov	dpl,r0
      001560 8B 83            [24] 3203 	mov	dph,r3
      001562 8C F0            [24] 3204 	mov	b,r4
      001564 C0 07            [24] 3205 	push	ar7
      001566 C0 06            [24] 3206 	push	ar6
      001568 C0 05            [24] 3207 	push	ar5
      00156A 12 07 7E         [24] 3208 	lcall	_configure_address
      00156D D0 05            [24] 3209 	pop	ar5
      00156F D0 06            [24] 3210 	pop	ar6
      001571 D0 07            [24] 3211 	pop	ar7
                                   3212 ;	src/radio.c:552: spi_write(W_TX_PAYLOAD, &data[2], data[0]);
      001573 74 02            [12] 3213 	mov	a,#0x02
      001575 2D               [12] 3214 	add	a,r5
      001576 FA               [12] 3215 	mov	r2,a
      001577 E4               [12] 3216 	clr	a
      001578 3E               [12] 3217 	addc	a,r6
      001579 FB               [12] 3218 	mov	r3,a
      00157A 8F 04            [24] 3219 	mov	ar4,r7
      00157C 8D 82            [24] 3220 	mov	dpl,r5
      00157E 8E 83            [24] 3221 	mov	dph,r6
      001580 8F F0            [24] 3222 	mov	b,r7
      001582 12 16 D1         [24] 3223 	lcall	__gptrget
      001585 FD               [12] 3224 	mov	r5,a
      001586 90 80 33         [24] 3225 	mov	dptr,#_spi_write_PARM_2
      001589 EA               [12] 3226 	mov	a,r2
      00158A F0               [24] 3227 	movx	@dptr,a
      00158B EB               [12] 3228 	mov	a,r3
      00158C A3               [24] 3229 	inc	dptr
      00158D F0               [24] 3230 	movx	@dptr,a
      00158E EC               [12] 3231 	mov	a,r4
      00158F A3               [24] 3232 	inc	dptr
      001590 F0               [24] 3233 	movx	@dptr,a
      001591 90 80 36         [24] 3234 	mov	dptr,#_spi_write_PARM_3
      001594 ED               [12] 3235 	mov	a,r5
      001595 F0               [24] 3236 	movx	@dptr,a
      001596 75 82 A0         [24] 3237 	mov	dpl,#0xa0
      001599 12 08 63         [24] 3238 	lcall	_spi_write
                                   3239 ;	src/radio.c:555: rfce = 1;
                                   3240 ;	assignBit
      00159C D2 90            [12] 3241 	setb	_rfce
                                   3242 ;	src/nRF24LU1P.h:35: inline void delay_us(uint16_t us) { do nop_us(); while(--us); }
      00159E 7E 0A            [12] 3243 	mov	r6,#0x0a
      0015A0 7F 00            [12] 3244 	mov	r7,#0x00
      0015A2                       3245 00220$:
      0015A2 00               [12] 3246 	nop 
      0015A3 00               [12] 3247 	nop 
      0015A4 00               [12] 3248 	nop 
      0015A5 00               [12] 3249 	nop 
      0015A6 1E               [12] 3250 	dec	r6
      0015A7 BE FF 01         [24] 3251 	cjne	r6,#0xff,00595$
      0015AA 1F               [12] 3252 	dec	r7
      0015AB                       3253 00595$:
      0015AB EE               [12] 3254 	mov	a,r6
      0015AC 4F               [12] 3255 	orl	a,r7
      0015AD 70 F3            [24] 3256 	jnz	00220$
                                   3257 ;	src/radio.c:557: rfce = 0;
                                   3258 ;	assignBit
      0015AF C2 90            [12] 3259 	clr	_rfce
                                   3260 ;	src/radio.c:560: while(true)
      0015B1                       3261 00175$:
                                   3262 ;	src/radio.c:563: rfcsn = 0;
                                   3263 ;	assignBit
      0015B1 C2 91            [12] 3264 	clr	_rfcsn
                                   3265 ;	src/radio.c:564: RFDAT = _NOP;
      0015B3 75 E5 FF         [24] 3266 	mov	_RFDAT,#0xff
                                   3267 ;	src/radio.c:565: RFRDY = 0;
                                   3268 ;	assignBit
      0015B6 C2 C0            [12] 3269 	clr	_RFRDY
                                   3270 ;	src/radio.c:566: while(!RFRDY);
      0015B8                       3271 00169$:
      0015B8 30 C0 FD         [24] 3272 	jnb	_RFRDY,00169$
                                   3273 ;	src/radio.c:567: rfcsn = 1;
                                   3274 ;	assignBit
      0015BB D2 91            [12] 3275 	setb	_rfcsn
                                   3276 ;	src/radio.c:570: if((RFDAT & TX_DS) == TX_DS)
      0015BD AE E5            [24] 3277 	mov	r6,_RFDAT
      0015BF 53 06 20         [24] 3278 	anl	ar6,#0x20
      0015C2 7F 00            [12] 3279 	mov	r7,#0x00
      0015C4 BE 20 EA         [24] 3280 	cjne	r6,#0x20,00175$
      0015C7 BF 00 E7         [24] 3281 	cjne	r7,#0x00,00175$
                                   3282 ;	src/radio.c:572: in1buf[0] = 1;
      0015CA 90 C6 80         [24] 3283 	mov	dptr,#_in1buf
      0015CD 74 01            [12] 3284 	mov	a,#0x01
      0015CF F0               [24] 3285 	movx	@dptr,a
                                   3286 ;	src/radio.c:578: write_register_byte(CONFIG, read_register_byte(CONFIG) | PRIM_RX);
      0015D0 75 82 00         [24] 3287 	mov	dpl,#0x00
      0015D3 12 09 71         [24] 3288 	lcall	_read_register_byte
      0015D6 E5 82            [12] 3289 	mov	a,dpl
      0015D8 90 80 3D         [24] 3290 	mov	dptr,#_write_register_byte_PARM_2
      0015DB 44 01            [12] 3291 	orl	a,#0x01
      0015DD F0               [24] 3292 	movx	@dptr,a
      0015DE 75 82 00         [24] 3293 	mov	dpl,#0x00
      0015E1 12 09 50         [24] 3294 	lcall	_write_register_byte
                                   3295 ;	src/radio.c:579: configure_address(pm_prefix, pm_prefix_length);
      0015E4 90 80 12         [24] 3296 	mov	dptr,#_pm_prefix_length
      0015E7 E0               [24] 3297 	movx	a,@dptr
      0015E8 FE               [12] 3298 	mov	r6,a
      0015E9 A3               [24] 3299 	inc	dptr
      0015EA E0               [24] 3300 	movx	a,@dptr
      0015EB 90 80 28         [24] 3301 	mov	dptr,#_configure_address_PARM_2
      0015EE EE               [12] 3302 	mov	a,r6
      0015EF F0               [24] 3303 	movx	@dptr,a
      0015F0 90 80 14         [24] 3304 	mov	dptr,#_pm_prefix
      0015F3 75 F0 00         [24] 3305 	mov	b,#0x00
      0015F6 12 07 7E         [24] 3306 	lcall	_configure_address
                                   3307 ;	src/radio.c:582: rfce = 1;
                                   3308 ;	assignBit
      0015F9 D2 90            [12] 3309 	setb	_rfce
                                   3310 ;	src/radio.c:583: in1bc = 1;
      0015FB 90 C7 B7         [24] 3311 	mov	dptr,#0xc7b7
      0015FE 74 01            [12] 3312 	mov	a,#0x01
      001600 F0               [24] 3313 	movx	@dptr,a
                                   3314 ;	src/radio.c:585: }
      001601 22               [24] 3315 	ret
                                   3316 	.area CSEG    (CODE)
                                   3317 	.area CONST   (CODE)
                                   3318 	.area XINIT   (CODE)
      001752                       3319 __xinit__nordic_bootloader:
      001752 00 78                 3320 	.byte #0x00,#0x78
      001754                       3321 __xinit__logitech_bootloader:
      001754 00 74                 3322 	.byte #0x00,#0x74
      001756                       3323 __xinit__promiscuous_address:
      001756 AA                    3324 	.db #0xaa	; 170
      001757 00                    3325 	.db #0x00	; 0
                                   3326 	.area CABS    (ABS,CODE)
