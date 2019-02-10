errors: u_L2_errors u_H1_errors v_L2_errors p_L2_errors

orders: u_L2_orders u_H1_orders v_L2_orders p_L2_orders


OUT_FILE=errors.out

u_L2_errors:
	cat $(OUT_FILE) | grep DG\ u\ error\ L2 | cut -d : -f 2 > $@.txt

u_H1_errors:
	cat $(OUT_FILE) | grep DG\ u\ error\ H1 | cut -d : -f 2 > $@.txt

v_L2_errors:
	cat $(OUT_FILE) | grep DG\ v\ error\ L2 | cut -d : -f 2 > $@.txt

p_L2_errors:
	cat $(OUT_FILE) | grep DG\ p\ error\ L2 | cut -d : -f 2 > $@.txt


u_L2_orders:
	cat $(OUT_FILE) | grep u,\ L2 | cut -d : -f 2 > $@.txt

u_H1_orders:
	cat $(OUT_FILE) | grep u,\ H1 | cut -d : -f 2 > $@.txt

v_L2_orders:
	cat $(OUT_FILE) | grep v,\ L2 | cut -d : -f 2 > $@.txt

p_L2_orders:
	cat $(OUT_FILE) | grep p,\ L2 | cut -d : -f 2 > $@.txt
