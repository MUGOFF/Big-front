from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from category.models import *
import joblib
from datetime import datetime, timedelta
from prophet import Prophet 

# Create your views here.
def forcast(request):
    model = Aimodel.objects.filter(select =True)[0]
    model_path = model.file.path
    print(model)
    print(model_path)
    # l=[]
    # files = request.FILES.getlist('files')
    # ans = request.POST.getlist('answer', '')
    # class_names = list(string.ascii_lowercase)
    # class_names = np.array(class_names)
    
    # # 모델 로딩
    # ai_model_arr = Aimodel.objects.filter(select=True)[0]
    # model_path = ai_model_arr.file.path
 #########################################################
    loaded_model = joblib.load(model_path)

    future = loaded_model.make_future_dataframe(periods=365)
    future['cap'] = (113860)
    future['floor'] = (8165)
    
    # for date in future['ds']:
    #     if date>datetime.today():
    future1 =future.loc[future['ds']>=datetime.today()-timedelta(days=1)].reset_index(drop=True)
    # future1 = future:].copy().reset_index(drop=True)

    forecast = loaded_model.predict(future1)

    # print(forecast['ds'].head(7))
    # print(forecast['ds'].head(7)[0])
    # print(forecast['yhat'].head(7))
    # print(forecast['yhat_lower'].head(7))
    # print(forecast['yhat_upper'].head(7))
    for n in range(7):
        category = SeoulAPI()
        category.ds = forecast['ds'].head(7)[n] 
        category.ythat = forecast['yhat'].head(7)[n] 
        category.yhat_lower = forecast['yhat_lower'].head(7)[n] 
        category.yhat_upper = forecast['yhat_upper'].head(7)[n]
        category.item = 'carrot'
        category.save() 
        print(category)
    
    # print(type(forecast['ds']))
########################################################
    # if os.path.splitext(model_path)[1] == '.h5':
    #     model = load_model(model_path)
    #     for idx,file in enumerate(files,start=0):
    #         if request.method == 'POST' and request.FILES['files']:
    #             # logger.error('file', file)
    #             # class names 준비
    #             # history 저장을 위해 객체에 담아서 DB에 저장한다.
    #             # 이때 파일시스템에 저장도 된다.
    #             r = Result()
    #             r.answer = ans[idx]
    #             r.image = file
    #             r.r_id = ai_model_arr.id
    #             r.pub_date = timezone.datetime.now()
    #             r.save()

    #             # 흑백으로 읽기
    #             img_path = np.fromfile(r.image.path,np.uint8)
    #             img= cv2.imdecode(img_path, cv2.IMREAD_GRAYSCALE)
    #             # img= cv2.imread(r.image.path, cv2.IMREAD_GRAYSCALE)
                
    #             # 크기 조정
    #             img = cv2.resize(img, (28, 28))

    #             # input shape 맞추기
    #             test_sign = img.reshape(1, 28, 28, 1)
    #             # test_sign = img.reshape(1, 784)
    #             # 스케일링
    #             test_sign = test_sign / 255.

    #             # 예측 : 결국 이 결과를 얻기 위해 모든 것을 했다.
    #             pred = model.predict(test_sign)
    #             pred_1 = pred.argmax(axis=1)

    #             #결과를 DB에 저장한다.
    #             r.result = class_names[pred_1[0]]
    #             if r.result==r.answer.lower() : r.bool=True
    #             else : r.bool=False
    #             l.append(r)
    #             r.save()
                
    #         # http method의 GET은 처리하지 않는다. 사이트 테스트용으로 남겨둠
    #         else:
    #             test = request.GET['test']
    #             logger.error(('Something went wrong!!',test))
    # else:
    #     print('model_path:',model_path)
    #     print('model_path type:',type(model_path))
    #     model = joblib.load(model_path)
    #     print('end')
    #     for idx,file in enumerate(files,start=0):
    #         if request.method == 'POST' and request.FILES['files']:
    #             # logger.error('file', file)
    #             # class names 준비
    #             # history 저장을 위해 객체에 담아서 DB에 저장한다.
    #             # 이때 파일시스템에 저장도 된다.
    #             r = Result()
    #             r.answer = ans[idx]
    #             r.image = file
    #             r.r_id = ai_model_arr.id
    #             r.pub_date = timezone.datetime.now()
    #             r.save()

    #             # 흑백으로 읽기
    #             img_path = np.fromfile(r.image.path,np.uint8)
    #             img= cv2.imdecode(img_path, cv2.IMREAD_GRAYSCALE)

    #             # 크기 조정
    #             img = cv2.resize(img, (28, 28))

    #             # input shape 맞추기
    #             #test_sign = img.reshape(1, 28, 28, 1)
    #             test_sign = img.reshape(1, 784)
    #             # 스케일링
    #             test_sign = test_sign / 255.

    #             # 예측 : 결국 이 결과를 얻기 위해 모든 것을 했다.
    #             pred = model.predict(test_sign)
    #             #pred_1 = pred.argmax(axis=1)

    #             #결과를 DB에 저장한다.
    #             r.result = class_names[pred[0]]
    #             if r.result==r.answer.lower() : r.bool=True
    #             else : r.bool=False
    #             l.append(r)
    #             r.save()
                
    #         # http method의 GET은 처리하지 않는다. 사이트 테스트용으로 남겨둠
    #         else:
    #             test = request.GET['test']
    #             logger.error(('Something went wrong!!',test))

    # context = {
    #     'result': l
    # }
    return HttpResponse(request,'Complete')
    # return render(request, 'language/result.html', context)


