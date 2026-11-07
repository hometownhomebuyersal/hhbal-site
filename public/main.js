(function(){
 // animated counters
 var els=document.querySelectorAll('[data-count]');
 if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;io.unobserve(e.target);var el=e.target,t=+el.dataset.count,s=el.dataset.suffix||'',t0=null;function f(ts){if(!t0)t0=ts;var p=Math.min((ts-t0)/1200,1);el.textContent=Math.round(t*p).toLocaleString('en-US')+s;if(p<1)requestAnimationFrame(f)}requestAnimationFrame(f)})},{threshold:.4});els.forEach(function(e){io.observe(e)})}
 // close mobile menu on click
 document.querySelectorAll('.nav a').forEach(function(a){a.addEventListener('click',function(){document.querySelector('.nav').classList.remove('open')})});
 // lead forms -> FormSubmit AJAX
 document.querySelectorAll('form.lead').forEach(function(f){
  f.addEventListener('submit',function(ev){
   ev.preventDefault();
   var msg=f.querySelector('.msg'),btn=f.querySelector('button[type=submit]');
   var addr=f.querySelector('[name=property_address]'),ph=f.querySelector('[name=phone]');
   msg.className='msg';
   if(!addr.value.trim()||ph.value.replace(/\D/g,'').length<10){msg.className='msg err';msg.innerHTML='Please enter the property address and a 10-digit phone number.';return}
   if(f.querySelector('[name=_honey]').value)return;
   var data={};new FormData(f).forEach(function(v,k){data[k]=v});
   if(!data.sms_consent)data.sms_consent='No';
   data.page=location.href;
   btn.disabled=true;btn.textContent='Sending…';
   fetch(f.action,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(data)})
   .then(function(r){return r.json().then(function(j){return {ok:r.ok,j:j}})})
   .then(function(res){if(res.ok&&String(res.j.success)!=='false'){f.reset();msg.className='msg ok';msg.innerHTML='<b>Thank you!</b> We got your info and will reach out shortly. Need us sooner? Call or text <a href="tel:+12059144215">205-914-4215</a>.'}else throw 0})
   .catch(function(){msg.className='msg err';msg.innerHTML='Sorry, that didn\u2019t go through. Please call or text <a href="tel:+12059144215">205-914-4215</a> or <a href="mailto:hometownhomebuyersal@gmail.com?subject=Cash%20offer%20request&body='+encodeURIComponent('Property: '+addr.value+'\nPhone: '+ph.value)+'">email us</a>.'})
   .finally(function(){btn.disabled=false;btn.textContent='Get Your Offer'});
  });
 });
})();
