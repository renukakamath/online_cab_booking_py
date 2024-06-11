from flask import * 
from database import*

from datetime import date



customer=Blueprint('customer',__name__)

@customer.route('/customer_home')
def customer_home():

	return render_template('customer_home.html')

@customer.route('/customer_updateprofile',methods=['post','get'])
def customer_updateprofile():
	data={}
	cid=session['customer_id']
	q="select * from customer where customer_id='%s'"%(cid)
	res=select(q)
	data['customerupdate']=res

	if "cusreg" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		h=request.form['hno']
		d=request.form['district']
		p=request.form['pin']
		n=request.form['num']
		q="update customer set customer_fname='%s',customer_lname='%s',customer_houser_name='%s',customer_dist='%s',customer_pincode='%s',customer_phone='%s' where customer_id='%s'"%(f,l,h,d,p,n,cid)
		update(q)
		flash('successfully')
		return redirect(url_for('customer.customer_updateprofile')) 

	return render_template('customer_updateprofile.html',data=data)




@customer.route('/customer_booking',methods=['post','get'])
def customer_booking():
	from datetime import date

	data={}
	today = date.today()
	print("Today's date:", type(today))
	data['m']=today
	print(today)




	q="select * from time where time_status='1'"
	res=select(q)
	data['timingview']=res


	q="select * from category where status='1'"
	res=select(q)
	data['categoryview']=res

	q="select * from location where location_status='1'"
	res=select(q)
	data['locationsview']=res

	

	if "Book" in request.form:
		time=request.form['time']
		location=request.form['location']
		category=request.form['category']
		total=request.form['total']
		cid=session['customer_id']

		# q="select * from booking where  time_id='%s'"%(date)
		# res=select(q)
		# if res:

		# 	flash('already Booked')

		# else:
			

		q="insert into booking values(null,'%s','%s','%s','%s','%s')"%(time,category,location,cid,total)
		insert(q)
		flash('successfully')
		# q="update boat set bstatus='0' where boat_id='%s'"%(bid)
		# update(q)
		return redirect(url_for('customer.customer_viewbooking'))
	
	return render_template('customer_booking.html',data=data)





@customer.route('/customer_viewbooking')
def customer_viewbooking():
	data={}
	cid=session['customer_id']
	q="SELECT * FROM `booking` INNER JOIN `time` USING (`time_id`) INNER JOIN `customer` USING (customer_id) INNER JOIN `category` USING (`category_id`)inner join location using (location_id) where customer_id='%s'" %(cid)
	res=select(q)
	print(q)
	data['bookingview']=res

	return render_template('customer_viewbooking.html',data=data)



@customer.route('/makepayment',methods=['post','get'])
def makepayment():
	data={}
	cid=session['customer_id']
	q="select * from card where customer_id='%s'"%(cid)
	res=select(q)
	data['carddrop']=res

	


	if "makepayment" in request.form:
		bid=request.args['bid']
		# amt=request.args['amt']
		cardno=request.form['cardno']


		q="insert into payment values(null,'%s' ,'0',curdate())"%(bid)
		insert(q)
		# q="update booking set status='Paid' where booking_id='%s'"%(bid)
		# update(q)
		flash('successfully')
		return redirect(url_for('customer.customer_viewbooking'))

	return render_template('makepayment.html',data=data)


@customer.route('/customer_addcard',methods=['post','get'])
def customer_addcard():
	if "card" in request.form:
		cid=session['customer_id']
		cardno=request.form['num']
		cardname=request.form['name']
		d=request.form['date']

		q="select * from card where customer_id='%s' and card_no='%s'"%(cid,cardno)
		res=select(q)
		if res:
			flash('already exist')

		else:


			from datetime import date,datetime

			d1=datetime.strptime(d,'%Y-%m')
			print(type(d1))


			today = datetime.today()
			print("Today's date:", type(today))

			print(d,")))))))))))")

			print(today)
			if d1 < today:
				flash('expired')
			else:
				q="insert into card values(null,'%s','%s','%s','%s')"%(cid,cardno,cardname,d)
				insert(q)
				flash('successfully')
				return redirect(url_for('customer.customer_viewbooking'))
	return render_template('customer_addcard.html')




# @customer.route('/payment',methods=['post','get'])
# def payment():
# 	data={}

# 	bid=request.args['bid']
# 	data['bid']=bid
# 	amt=request.args['ttamount']
# 	data['ttamount']=amt
	

	
# 	cid=session['customer_id']
# 	q="select * from card where customer_id='%s'"%(cid)
# 	res=select(q)
# 	data['card']=res



# 	if "confirm_order" in request.form:
# 		bid=request.args['bid']
# 		amt=request.args['ttamount']
# 		cnum=request.form['cnum']
# 		cname=request.form['cname']
# 		cid=session['customer_id']
		
# 		d=request.form['date']


# 		from datetime import date,datetime

# 		d1=datetime.strptime(d,'%Y-%m')
# 		print(type(d1))


# 		today = datetime.today()
# 		print("Today's date:", type(today))

# 		print(d,")))))))))))")

# 		print(today)
# 		if d1 < today:


# 			flash('expired')




# 		else:
# 			  q="UPDATE `booking` SET `status`='paid' WHERE `booking_id`='%s'"%(bid)
# 			  update(q)
# 			  q2="INSERT INTO `payment` VALUES(NULL,'%s','%s',CURDATE())"%(bid,amt)
# 			  insert(q2);
# 			  q="SELECT * FROM `card` WHERE `card_no`='%s' AND `card_name`='%s'  and `customer_id`='%s'"%(cnum,cname,cid)
# 			  res=select(q)
# 			  if len(res) == 0:
# 			  	q3="INSERT INTO `card` VALUES(NULL,'%s','%s','%s','%s')"%(cid,cnum,cname,d)
# 			  	insert(q3);
# 			  return redirect(url_for('customer.customer_viewbooking'))
			  
			
		


# 	if "action" in request.args:
# 		action=request.args['action']
# 		choose=request.args['choose']

# 		if action=='choose':
# 			qx="SELECT * FROM `card`  WHERE `card_id`='%s'"%(choose)
# 			rx=select(qx);
# 			data['chooses']=rx
# 	return render_template('payment.html',data=data)


