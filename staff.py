from flask import * 
from database import*
import uuid



staff=Blueprint('staff',__name__)

@staff.route('/staff_home')
def staff_home():

	return render_template('staff_home.html')
@staff.route('/staff_managestaff',methods=['post','get'])
def staff_managestaff():
	data={}
	q="select * from staff inner join login using (username)"
	res=select(q)
	
	data['staffview']=res

	if "action" in request.args:
		action=request.args['action']
		uid=request.args['uid']

		if action=='active':
			q="update login set `status`='1' where username='%s'"%(uid)
			update(q)

			q="update staff set `staff_status`='1' where username='%s'"%(uid)
			update(q)
			flash('successfully')
			return redirect(url_for('staff.staff_managestaff'))
		
		if action=='inactive':
			q="update login set `status`='0' where username='%s'"%(uid)
			update(q)
			q="update staff set `staff_status`='0' where username='%s'"%(uid)
			update(q)
			flash('successfully')
			return redirect(url_for('staff.staff_managestaff'))


		if action=='update':
			q="select * from staff"
			res=select(q)
			data['staffupdate']=res

		if "update" in request.form:
			f=request.form['fname']
			l=request.form['lname']
			d=request.form['date']
			ho=request.form['hno']
			
			ha=request.form['hna']
			
			di=request.form['district']
			p=request.form['pin']
			g=request.form['gen']
			
			
			n=request.form['num']
			
			q="update staff set staff_fname='%s',staff_lname='%s',staff_gender='%s',staff_dob='%s',staff_house_name='%s',staff_house_no='%s',staff_dist='%s',staff_pincode='%s',staff_phone='%s' where username='%s'"%(f,l,g,d,ha,ho,di,p,n,uid)
			update(q)
			print(q)
			print(q)
			flash('successfully')

			return redirect(url_for('staff.staff_managestaff'))
	

	if "staffreg" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		d=request.form['date']
		ho=request.form['hno']
		
		ha=request.form['hna']
		
		di=request.form['district']
		p=request.form['pin']
		g=request.form['gen']
		
		
		n=request.form['num']
		u=request.form['uname']
		pa=request.form['pwd']
		q="insert into login values('%s','%s','staff','1')"%(u,pa)
		insert(q)
		q="insert into staff values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','1')"%(u,f,l,d,ho,ha,di,p,g,n)
		insert(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managestaff'))


	return render_template('staff_managestaff.html',data=data)


@staff.route('/staff_managecategory',methods=['post','get'])	
def staff_managecategory():
	data={}
	q="select * from category"
	res=select(q)
	data['categoryview']=res

	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']

	else:
		action=None

	if action=='active':
		q="update category set status='1' where category_id='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managecategory'))
	if action=='inactive':
		q="update category set status='0' where category_id='%s'"%(cid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managecategory'))

	if action=='update':
		q="select * from category where category_id='%s'"%(cid)
		res=select(q)

		data['categoryupdate']=res

	if "update" in request.form:
		f=request.form['fname']

		description=request.form['description']
		
		q="update category set category_name='%s' ,cat_decription='%s' where category_id='%s'"%(f,cid,description)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managecategory'))
	if "category" in request.form:
		f=request.form['fname']
		description=request.form['description']
		
		q="insert into category values(null,'%s','%s','1')"%(f,description)
		insert(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managecategory'))
		
	return render_template('staff_managecategory.html',data=data)

@staff.route('/staff_managetime',methods=['post','get'])
def staff_managetime():
	data={}
	q="select * from time"
	res=select(q)
	data['subview']=res

	if "action" in request.args:
		action=request.args['action']
		sid=request.args['sid']

	else:
		action=None


	if action=='active':
		q="update time set time_status='1' where time_id='%s'"%(sid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managetime'))

	if action=='inactive':
		q="update time set time_status='0' where time_id='%s'"%(sid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managetime'))

	if action=='update':
		q="select * from time where time_id='%s'"%(sid)
		res=select(q)
		data['timeupdate']=res


	if "update" in request.form:
		f=request.form['fname']
		
		q="update time set time_slot='%s' where time_id='%s'"%(f,sid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managetime'))

			
			
			

	if "time" in request.form:
		f=request.form['fname']
		
		q="insert into time values(null,'%s','1')"%(f)
		insert(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managetime'))

	return render_template('staff_managetime.html',data=data)



@staff.route('/staff_managelocation',methods=['post','get'])
def staff_managelocation():
	data={}
	q="select * from location"
	res=select(q)
	data['subview']=res

	if "action" in request.args:
		action=request.args['action']
		sid=request.args['sid']

	else:
		action=None


	if action=='active':
		q="update location set location_status='1' where location_id='%s'"%(sid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managelocation'))

	if action=='inactive':
		q="update location set location_status='0' where location_id='%s'"%(sid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managelocation'))

	if action=='update':
		q="select * from location where location_id='%s'"%(sid)
		res=select(q)
		data['subcategoryupdate']=res


	if "update" in request.form:
		f=request.form['slo']
		e=request.form['elo']
		
		q="update location set start_location='%s', end_location='%s' where location_id='%s'"%(f,e,sid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managelocation'))

			
			
			

	if "location" in request.form:
		f=request.form['slo']
		e=request.form['elo']
		
		q="insert into location values(null,'%s','%s','1')"%(f,e)
		insert(q)
		flash('successfully')
		return redirect(url_for('staff.staff_managelocation'))

	return render_template('staff_managelocation.html',data=data)




@staff.route('/staff_viewcustomer')	
def staff_viewcustomer():
	data={}

	if "action" in request.args:
		action=request.args['action']
		lid=request.args['lid']

	else:
		action=None

	if action=='accept':
		q="update login set status='1' where username='%s'"%(lid)
		update(q)
		q="update customer set customer_status='1' where username='%s'"%(lid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_viewcustomer'))

	if action=='reject':
		q="update login set status='0' where username='%s'"%(lid)
		update(q)
		q="update customer set customer_status='0' where username='%s'"%(lid)
		update(q)
		flash('successfully')
		return redirect(url_for('staff.staff_viewcustomer'))
			
	q="select * from customer inner join login using (username)"
	res=select(q)
	data['customerview']=res

	return render_template('staff_viewcustomer.html',data=data)



@staff.route('/staff_viewbooking')
def staff_viewbooking():
	data={}
	q="SELECT * FROM `booking` INNER JOIN `time` USING (`time_id`) INNER JOIN `customer` USING (customer_id) INNER JOIN `category` USING (`category_id`)inner join location using (location_id) "
	res=select(q)
	data['bookingview']=res
	return render_template('staff_viewbooking.html',data=data)	



@staff.route('/staff_viewpayment')
def staff_viewpayment():
	data={}
	bid=request.args['bid']
	q="SELECT * FROM `payment`  INNER JOIN `booking` USING (`booking_id`) INNER JOIN `customer` USING (`customer_id`) where booking_id='%s'"%(bid)
	res=select(q)
	data['paymentview']=res

	return render_template('staff_viewpayment.html',data=data)	


@staff.route('/staff_managereport',methods=['post','get'])	
def staff_managereport():
	data={}
	if "sale" in request.form:
		daily=request.form['daily']
		if request.form['monthly']=="":
			monthly=""
		else:
			monthly=request.form['monthly']+'%'
		print(monthly)
		customer=request.form['customer']	
		q="SELECT * FROM `booking` INNER JOIN `time` USING (`time_id`) INNER JOIN `customer` USING (customer_id) INNER JOIN `category` USING (`category_id`)inner join location using (location_id) inner join payment using(booking_id) where (`customer_fname` like '%s') or (`date` like '%s'  ) or (`date` like '%s' ) "%(customer,daily,monthly)
		res=select(q)
		print(q)
		data['report']=res
		session['res']=res
		r=session['res']
	else:
		q="SELECT * FROM `booking` INNER JOIN `time` USING (`time_id`) INNER JOIN `customer` USING (customer_id) INNER JOIN `category` USING (`category_id`)inner join location using (location_id) inner join payment using(booking_id)"
		res=select(q)
		data['report']=res
	
	return render_template('staff_managereport.html',data=data)

@staff.route('/staff_salesreport')
def staff_salesreport():
	data={}

	r=session['res']
	data['r']=r


	return render_template('staff_salesreport.html',data=data)	






