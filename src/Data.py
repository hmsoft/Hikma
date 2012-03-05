#!/usr/bin/env python
#! -*- coding:WINDOWS-1256 -*-
# Data.py

import random

database = [
'ابذل لصديقك دمك ومالك.' ,
'إبرة في كومة قش.' ,
'أتبع من الظل.' ,
'اتَّكَلْنا منه على خُصٍّ.' ,
'الاتحاد قوة.' ,
'اترك الشر يتركك.' ,
'اتسع الخرق على الراقع.' ,
'اتسقني ماء الحياة بذلة بل فاسقني بالعز كأس الحنظل.' ,
'أثقل من جبل.' ,
'اجتنب مصاحبة الكذاب فإن اضطررت إليه فلا تُصَدِّقْهُ.' ,
'اجلس حيث يُؤْخَذُ بيدك وَتُبَرُّ ولا تجلس حيث يؤخذ برجلك وتُجَرُّ.' ,
'أجهل الناس من كان على السلطان مدلا وللإخوان مذلا.' ,
'احذر الأحمق واحذر وُدَّهُ.' ,
'احذر عدوك مرة وصديقك ألف مرة فإن انقلب الصديق فهو أعلم بالمضرة.' ,
'أحذر من غراب.' ,
'احذروا من لا يرجى خيره ولا يؤمن شره.' ,
'أحرس من كلب.' ,
'أَحْسِنْ إلي الناس تستعبد قلوبهم.' ,
'أحضر الناس جوابا من لم يغضب.' ,
'احفر بئرا وَطُمَّ بئرا ولا تُعَطِّلْ أجيرا.' ,
'احفظ قرشك الأبيض ليومك الأسود.' ,
'أحمد البلاغة الصمت حين لا يَحْسُنُ الكلام.' ,
'أحن من الأم على أولادها.' ,
'آخ الأْكْفاءَ وداه الأعداء.' ,
'أخاك أخاك إن مَنْ لا أخا له كَساعٍ إلى الهيجا بغير سلاح.' ,
'اختر أهون الشرين.' ,
'اختلط حابلهم بنابلهم.' ,
'آخر الحياة الموت.' ,
'اخطب لابنتك و لا تخطب لابنك.' ,
'أَخْفَقَ حالب التيس.' ,
'أخوك من صدقك النصيحة.' ,
'أخوك من صَدَقك لا من صدّقك.' ,
'أَدّى قدراً مستعيرها.' ,
'أدنى من حبل الوريد.' ,
'إذا أتت مذمتي من ناقص فهي الشهادة لي بأني كامل.' ,
'إذا أردت أن تطاع فأمر بما يستطاع.' ,
'إذا الشعب يوما أراد الحياة فلا بد أن يستجيب القدر.' ,
'إذا المرء لم يدنس من اللؤم عرضه فكل رداء يرتديه جميل.' ,
'إذا أنت أكرمت الكريم ملكته و إن أنت أكرمت اللئيم تمردا.' ,
'إذا أنت لم تشرب مرارا على القذى ظمئت وأي الناس تصفو مشاربه.' ,
'إذا بلغ الرأي المشورة فاستعن بحزم ناصح أو نصيحة حازم.' ,
'إذا تخاصم اللصان ظهر المسروق.' ,
'إذا تفرقت الغنم قادتها العنز الجرباء.' ,
'إذا تكلمت بالكلمة ملكتك و إذا لم تتكلم بها ملكتها.' ,
'إذا تم العقل نقص الكلام.' ,
'إذا تمنيت فاستكثر.' ,
'إذا تولى عقداً أحكمه.' ,
'إذا حان القضاء ضاق الفضاء.' ,
'إذا حضر الماء بطل التيمم.' ,
'إذا دببت على المنسأة من هرم فقد تباعد عنك اللهو والغزل.' ,
'إذا ذكرت الذئب فأعد له العصا.' ,
'إذا ذكرت الذئب فخذ الحذر.' ,
'إذا ذل مولى فهو ذليل.' ,
'إذا رأيت نيوب الليث بارزة فلا تظنن أن الليث يبتسم.' ,
'إذا زل العالِمُ زل بزلته عالَمٌ.' ,
'إذا ساء فعل المرء ساءت ظنونه وَ صَدَّقَ ما يعتاده من توهم.' ,
'إذا سأل ألحف و إن سئل سوّف.' ,
'إذا سلمت من الأسد فلا تطمع في صيده.' ,
'إذا سمعت الرجل يقول فيك من الخير ما ليس فيك فلا تأمن أن يقول فيك من الشر ما ليس فيك.' ,
'إذا صدأ الرأي أصقلته المشورة.' ,
'إذا صُنْتَ المودة كان باطنها أحسن من ظاهرها.' ,
'إذا ضربت فأوجع فإن الملامة واحدة.' ,
'إذا ظلمت من دونك فلا تأمن عقاب من فوقك.' ,
'إذا عُرِفَ السبب بطل العجب.' ,
'إذا غامَرْتَ في شرف مروم فلا تقنع بما دون النجوم.' ,
'إذا فرغ الفؤاد ذهب الرقاد.' ,
'إذا قصرت يدك عن المكافأة فليصل لسانك بالشكر.' ,
'إذا قل ماء الوجه قل حياؤه.' ,
'إذا كان الصبر مُرًّا فعاقبته حلوة.' ,
'إذا كان الكلام من فضة فالسكوت من ذهب.' ,
'إذا كنت تدري فتلك مصيبة و إن كنت لا تدري فالمصيبة أعظم.' ,
'إذا كنت ذا رأي فكن ذا عزيمة.' ,
'إذا كنتَ ذا رأىٍ فكن ذا مشورة فإن فساد الرأي أن تترددا.' ,
'إذا كنت سنداناً فاصبر و إذا كنت مطرقة فأوجع.' ,
'إذا كنت في كل الأمور معاتبا صديقك لم تلق الذي لا تعاتبه.' ,
'إذا لم يكن إلا الأَسِنَّةُ مركبا فلا رأي للمضطر إلا ركوبها.' ,
'إذا لم ينفعك البازي فانتف ريشه.' ,
'إذا نُصِرَ الرأي بطل الهوى.' ,
'إذا هَبَّتْ رياحك فاغتنمها.' ,
'اذالم تستحي فأفعل ما تشاء.' ,
'أذل البخل أعناق الرجال.' ,
'أرخص من التمر في البصرة.' ,
'أرسل حكيما و لا توصه.' ,
'أرى كل إنسان يرى عيب غيره و يعمى عن العيب الذي هو فيه.' ,
'ازرع كل يوم تأكل.' ,
'أساء سمعا فأساء إجابة.' ,
'استر عورة أخيك لما يعلمه فيك.' ,
'استقبال الموت خير من استدباره.' ,
'استندت إلى خصٍ مائلٍ.' ,
'استنوق الجمل.' ,
'أسد عليَّ و في الحروب نعامة.' ,
'أسرع من الريح.' ,
'أسمع جعجعة و لا أرى طحنا.' ,
'الإشارات تُغْني اللبيب عن العبارات.' ,
'اشتدي يا أزمة تنفرجي.' ,
'أشد الجهاد مجاهدة الغيظ.' ,
'أشد الفاقة عدم العقل.' ,
'اشكر من أَنْعَمَ عليك و أَنْعِمْ على من شكرك.' ,
'اصبر تنل.' ,
'اصبر قليلا فبعد العسر تيسير و كل أمر له وقت و تدبير.' ,
'اصبر لكل مُصِيبةٍ و تجلًّدِ و اعلم بأن الدهر غير مُخَلَّدِ.' ,
'أصحاب العقول في نعيم.' ,
'أصحابي كالنجوم بأيهم اقتديتم اهتديتم.' ,
'إصلاح الموجود خير من انتظار المفقود.' ,
'اضحك يضحك العالم معك و ابك تبك وحدك.' ,
'اِضْرِبْ ما دام الحديد حامياً.' ,
'أضعت شاة جعلت الذئب حارسها أما علمت بأن الذئب حراس.' ,
'أضيق الأمر أدناه من الفرج.' ,
'اطلب تظفر.' ,
'اطلب من العلوم علماً ينفعك ينفي الأذى والعيب ثم يرفعك.' ,
'اطلبوا العلم من المهد إلى اللحد.' ,
'اطلبوا العلم و لو في الصين.' ,
'أطهر الناس أعراقاً أحسنهم أخلاقاً.' ,
'أظلم من أفعى.' ,
'أعدّوا لكلب السوء كلبا يعادله.' ,
'أعدل الشهود التجارب.' ,
'أعرف الناس بالله أرضاهم بما قسم الله له.' ,
'اعرف صاحبك واتركه.' ,
'أعز مكان في الدنا سرج سابح و خير جليس في الزمان كتاب.' ,
'أعز من الولد ولد الولد.' ,
'أعزب دهر و لا أرمل شهر.' ,
'أعط الخبز لخبازه و لو أكل نصفه.' ,
'أعط القوس باريها.' ,
'اعطني عمر و ارميني بالبحر.' ,
'اعف عما أغضبك لما أرضاك.' ,
'أَعقَلُ الناس أَعْذَرُهُمْ للناس.' ,
'اعقلها و توكل.' ,
'أعلمه الرماية كل يوم فلما أشتد ساعِدُهُ رماني.' ,
'أعلى الممالك ما يبنى على الأسل.' ,
'اعمل الطيب وارمه البحر.' ,
'الأعور في وسط العميان ملك.' ,
'أغن من وليته عن السرقة.' ,
'أغنى الأغنياء من لم يكن للبخل أسيراً.' ,
'أغيرة و جبنًا؟' ,
'أغيظ من عاداك من لا تُشَاكِلُ.' ,
'آفة الحديث الكذب.' ,
'آفة الرأي الهوى.' ,
'آفة العِلْم النسيان.' ,
'الإفراط في التواضع يجلب المذلة.' ,
'أفْضَلُ الجهاد كلمة عدل عند سلطان جائر.' ,
'أفضل الجود العطاء قبل الموعد.' ,
'أفضل الجود أن تبذل من غير مسألة.' ,
'الأفعال أبلغ من الأقوال.' ,
'الاقتصاد في النفقة نصف المعيشة.' ,
'أقرب من اللسان للأسنان.' ,
'أقل الناس سروراً الحسود.' ,
'قلل طعامك تجد منامك.' ,
'قلل عتابك فالبقاء قليل و الدهر يعدل تارة و يميل.' ,
'أكبر منك بيوم يعرف عنك بسنة.' ,
'اكذب النفس إذا حدثتها.' ,
'إكرام الميت دفنه.' ,
'أكرم نفسك عن كل دنيء.' ,
'أكل و حمد خير من أكل و صمت.' ,
'أكلوا خيري و عصوا أمري.' ,
'ألا كل ما هو آت قريب و للأرض من كل حي نصيب.' ,
'ألقاب مملكة في غير موضعها كالهر يحكي انتفاخا صولة الأسد.' ,
'ألقمه الحجر.' ,
'إلى التراب يصير الناس كلهم.' ,
'إلى حتفي مَشَتْ قدمي.' ,
'الأم مدرسة إذا أعددتها أعددت شعباً طيب الأعراق.' ,
'الإمارة حلوة الرضاع مُرَّةُ الفطام.' ,
'إمام فعال خير من إمام قَوَّالٍ.' ,
'الأماني حلم في يقظة و المنايا يقظة من حلم.' ,
'الأماني رءوس مال المفاليس.' ,
'الأمر يعرض دونه الأمر.' ,
'أملك الناس لنفسه من كتم سره.' ,
'إن أخاك من واساك.' ,
'إن الأيادي قروض.' ,
'إن البعوضة تُدْمي مُقْلةَ الأسد.' ,
'إن البغاث بأرضنا يستنسر' ,
'إن الجبان حتْفُه من فوقه' ,
'إن الجواد قد يعثر' ,
'إن الحياة عقيدة وجهاد' ,
'إن الذليل من دل في سلطانه' ,
'إن السفينة لا تجري على اليابس' ,
'إن السماء تُرْجَى حين تحتجب' ,
'إن الشباب والفراغ والْجِدَة مفسدة للمرء أي مفسدة' ,
'إن الشفيق بسوء ظن مولع' ,
'إن الغصون إذا قومتها اعتدلت' ,
'إن الغنى والعز في القناعة والذل في الحرص وفي الوضاعة' ,
'إن القذى يؤذي العيون قليله ولربما جرح البعوض الفيلا' ,
'إن الله جَوَّادٌ يحب كل جَوَّادٍ' ,
'إن الله يحب معالي الأمور ويبغض سفاسفها' ,
'إن الله يمهل ولا يهمل' ,
'إن المعاذير يَشُوبُها الكذب' ,
'إن المعارف في أهل النهى ذمم' ,
'إن المعلم لم تكن أقواله طبق الفعال فقوله لن يثمرا' ,
'إن المقْدِرة تُذْهِبَ الحفيظة' ,
'إن جهد المقل غير قليل' ,
'إن زاد الشيء عن حده ينقلب لضده' ,
'إن غدا لناظره قريب' ,
'إن غلا اللحم فالصبر رخيص' ,
'إن قل مالي فلا خِلُّ يصاحبني وإن زاد مالي فكل الناس خِلاَّنِي' ,
'إن كبر ابنك آخيه' ,
'إن كنت ريحا فقد لاقيت إعصارا' ,
'إن كنت كذوباً فكن ذكوراً' ,
'إن لم يكن وفاق ففراق' ,
'إن مع اليوم غدا يا مسعدة' ,
'إن مفاتيح الأمور العزائم' ,
'إن من البيان لسحرا' ,
'إن نبغتم ففي علم وفي أدب وفي صناعات عصر ناسه صُنع' ,
'إن وراء الأَكَمةِ ما وراءها' ,
'أنا الغريق فما خوفي من البلل' ,
'أنا لها ولكل عظيمة' ,
'أنت على رد ما لم تقل أقدر منك على رد ما قلت' ,
'انتظر حتى يشيب الغراب' ,
'أنجز حر ما وعد' ,
'الإنسان بالتفكير والله بالتدبي' ,
'أنفس ما للفتى لُبُّهُ' ,
'أنفك منك ولو كان أجدع' ,
'إنك تضرب في حديد بارد' ,
'إنما سُمِّيتَ هانئاً لتهنأ' ,
'إنه لأشبه به من التمرة بالتمرة' ,
'إنه نسيج وحده' ,
'أهل مكة أدرى بشعابها' ,
'أول الحزم المشورة' ,
'أول الشجرة بذرة' ,
'أول الشجرة بذرة' ,
'أول الغضب جنون وآخره ندم' ,
'أول القصيدة كفر' ,
'أول ما شطح نطح' ,
'أولى الناس بالعفو أقدرهم على العقوبة' ,
'إياك عني واسمعي يا جارة' ,
'إياك وأن يضرب لسانك عنقك' ,
'إياك وصاحب السوء فإنه يحسن منظره ويقبح أثره' ,
'إياك وما يعتذر منه' ,
'الأيام دول' ,
'بئس الشعار الحسد' ,
'الباب الذي يأتيك بالريح سده واسترح' ,
'باب النجار مخَلَّع' ,
'باع كرمه واشترى معصرة' ,
'بالأرض ولدتك أمك' ,
'بالتأني تُدْرَكُ الفُرَصُ' ,
'بالرفاء والبنين' ,
'البخيل عظيم الرواق صغير الأخلاق' ,
'البخيل غناه فقر ومطبخه قفر' ,
'البخيل لا تَبُلُّ إحدى يديه الأخرى' ,
'بدن فاجر وقلب كافر' ,
'بذات فمه يفتضح الكذوب' ,
'بِشْرُ الكريم في وجهه يلوح' ,
'الْبِشْرَ دال على الكرم' ,
'البِشْر يعقد القلوب على المحبة' ,
'البصر بالزَّبُونِ تجارة' ,
'البطن لا تلد عدواً' ,
'البطنة تزيل الفطنة' ,
'بُعد السما من الأرض' ,
'البعد جفاء' ,
'بعض الحلم ذل' ,
'بعض الشر أهون من بعض' ,
'بعض الشر أهون من بعض' ,
'بعض العفو ضعف' ,
'بغاث الطير أكثرها فراخاً' ,
'بقدر الرأي تعتبر الرجال وبالآمال ينتظر المآل' ,
'بقدر لُغاتِ المرء يَكْثُرُ نفعه' ,
'بلغ السكين العظم' ,
'بلغ السيل الزُّبَى' ,
'بنفسي فَخَرْتُ لا بجدودي' ,
'البياض نصف الحسن' ,
'بيت الظالم خراب' ,
'بيت المحسن عمار' ,
'بيتي أستر لعوراتي' ,
'بين وعده وإنجازه فترة نبي' ,
'بينهم داء الضرائر' ,
'تأبى الدراهم إلا كشف أرؤسها إن الغني طويل الذيل مياس' ,
'تأبي الرماح إذا اجتمعن تكسرا وإذا افترقن تكسرت أفرادا' ,
'تاج المروءة التواضع' ,
'تألف النعمة بحسن جوارها' ,
'التأني من الرحمن والعجلة من الشيطان' ,
'التَّحَسُّنُ خير من الْحُسْنِ' ,
'التجارب ليست لها نهاية والمرء منها في زيادة' ,
'التجربة العلم الكبير' ,
'تجربة المجرب تضييع للأيام' ,
'تجري الرياح بما لا تشتهي السفن' ,
'تجوع الحرة ولا تأكل بثدييها' ,
'التدبير نصف المعيشة' ,
'التدبير يثمر اليسير والتبذير يبدد الكثير' ,
'ترك الذنب أيسر من الاعتذار' ,
'تركتهم في حيص بيص' ,
'تركه غنيمة والظفر به هزيمة' ,
'التسلُّطُ على المماليك دناءة' ,
'تطلب أثراً بعد عين' ,
'تعاشروا كالإخوان وتحاسبوا كالغرباء' ,
'تعاشروا كالإخوان وتعاملوا كالأغراب' ,
'تعدو الذئاب على من لا كلاب له وتتقي صولة المستنفر الحامي' ,
'تعلم فليس المرء يولد عالما وليس أخو علم كمن هو جاهل' ,
'تفرقوا أيدي سبأ' ,
'تقاربوا بالمودة ولا تتكلوا على القرابة' ,
'تقطع أعناق الرجال المطامع' ,
'تكاثرت الظباء على خراش فما يدري خراش ما يصيد' ,
'التكبر على المتكبر تواضع' ,
'تكلم فقد كلم الله موسى' ,
'تمام الصدق الإخبار بما تحمله العقول' ,
'تمخض الجبل فولد فأرا' ,
'تناس مساوئ الإخوان يدم لك وُدُّهُمْ' ,
'التواضع من مصائد الشرف' ,
'توبة الجاني واعتذاره' ,
'الثروة تأتي كالسلحفاة وتذهب كالغزال' ,
'جاء لك الموت يا تارك الصلاة' ,
'جاءوا عن بكرة أبيهم' ,
'الجار أولى بالشُّفْعَةِ' ,
'الجار قبل الدار' ,
'جاهدوا أهواءكم كما تجاهدون أعداءكم' ,
'جزاء مُجيرِ أُمِّ عامِرٍ' ,
'الجزاء من جنس العمل' ,
'الجزع عند المصيبة مصيبة' ,
'جليس المرء مثله' ,
'جمعت أمرين ضاع الحزم بينهما تيه الملوك وأفعال المماليك' ,
'الجنة بدون ناس لا تُداس' ,
'جنت على نفسها براقش' ,
'جَنَّةُ الرجل داره' ,
'الجهل شر الأصحاب' ,
'الجهل موت الأحياء' ,
'جواهر الأخلاق تصفها المعاشرة' ,
'الجود بالنفس أقصى غاية الجود' ,
'الجود من الموجود' ,
'الجوع كافر' ,
'جولة الباطل ساعة وجولة الحق إلى قيام الساعة' ,
'الحاجة تفتق الحيلة' ,
'حاسد النعمة لا يرضيه إلا زوالها' ,
'الحاسد يرى زوال نعمتك نعمة عليه' ,
'حافٍ يسخر بناعل' ,
'الحب أعمى' ,
'حب الوطن من الإيمان' ,
'حبر على ورق' ,
'حبل الكذب قصير' ,
'حج والناس راجعون' ,
'الحر تكفيه الإشارة' ,
'حرامي بلا بَيِّنةٍ شريف' ,
'الحرب سجال' ,
'الحركة بركة' ,
'حسب الحليم أن الناس أنصاره على الجاهل' ,
'حسبك من الشر سماعه' ,
'حسبه صيدا فكان قيدا' ,
'الحسد ثِقْلٌ لا يضعه حامله' ,
'الحسد داء لا يبرأ منه' ,
'الحسد والنفاق والكذب أثافي الذل' ,
'حُسْنُ الخلق خير قرين' ,
'حُسْنُ الخلق يذيب الخطايا كما تذيب الشمس الجليد' ,
'حُسْنُ الخلق يوجب المودة' ,
'حُسْنُ الصورة جمال الظاهر وَحُسْنُ العقل جمال الباطن' ,
'الحسود لا يَسُودُ' ,
'الحصاة من الجبل' ,
'حظ في السحاب وعقل في التراب' ,
'حفظ السر أمانة' ,
'حِفْظُ اللسان راحة الإنسان' ,
'الحق أبْلَجُ والباطل لجلج' ,
'الحق دولة والباطل جولة' ,
'الحق ظل ظليل' ,
'حق على ابن الصقر أن يشبه الصقر' ,
'حق من كتب بمسك أن يختم بعنبر' ,
'الحق يعلو ولا يعلى عليه' ,
'الحِلْم أجَلُّ من العقل' ,
'الحِلْمُ سيد الأخلاق' ,
'الحليم مطية الجهول' ,
'حِمَاكَ أحمى لك وأهلك أحفى بك' ,
'الحُمْقُ داء ولا دواء له' ,
'حمى الوطيس' ,
'حوالينا لا علينا' ,
'الحي أبقى من الميت' ,
'حياة المرء ثوب مستعار' ,
'حيلة العاجز دموعه' ,
'خادم سيدين يكذب على أحدهما' ,
'الخاذل أخو القاتل' ,
'خاطر من استغنى برأيه' ,
'خالف تُعْرَفْ' ,
'خالف هواك ترشد' ,
'خدعوها بقولهم "حسناء" والغواني يَغُرُّهُنَّ الثناء' ,
'خُذْهُ بالموت حتى يرضى بالحُمَّى' ,
'خذو الحكمة من أفواه البسطاء' ,
'خرج من المولد بلا حُمّص' ,
'خلا لك الجو فبيضي واصفري' ,
'خلقت مُبَرَّأً من كل عيب كأنك قد خُلقْتَ كما تشاء' ,
'خير الإخوان أقدمهم' ,
'خير الأشياء جديدها' ,
'خير الأصدقاء من ترك المزاح' ,
'خير الأعمال ما كان ديمة' ,
'خير الأمور أوساطها' ,
'خير البر عاجله' ,
'خير الخلال حفظ اللسان' ,
'خير الكلام ما قل ودل' ,
'خير المال ما وَجَّهْتَهُ وِجْهتَه' ,
'خير المحادث والجليس كتاب تخلو به إن ملّك الأصحاب' ,
'خير الناس للناس خيرهم لنفسه' ,
'خير الناس من فرح للناس بالخير' ,
'خير جليس في الزمان كتاب' ,
'خير صِلاتِ الكريم أَعْوَدُها' ,
'الخير على قدوم الواردين' ,
'خير مالك ما نفعك' ,
'الخَيْرُ يُخَيِّر والشر يغَيّر' ,
'الخيل أعرف بفارسها' ,
'داء الجهل ليس له دواء' ,
'الدال على الخير كفاعله' ,
'داوني بالتي كانت هي الداء' ,
'دخان الأقارب يُعمِي' ,
'الدراهم مراهم' ,
'درهم وقاية خير من قنطار علاج' ,
'دع الأيام تفعل ما تشاء وطب نفسا بما حكم القضاء' ,
'دع عنك لومي فإن اللوم إغراء' ,
'دع ما أنكرت لما عَرَفْتَ' ,
'دِعَامَةُ العقل الحلم' ,
'دل على عاقل اختياره' ,
'الدم لا يصير ماء' ,
'الدنيا سجن المؤمن وجنة الكافر' ,
'دنياك ما أنت فيه' ,
'الدهر يومان حلو ومر' ,
'دواء الدهر الصبر عليه' ,
'الدين النصيحة' ,
'ذا جاء الحين حارت العين' ,
'ذكر الفتى عمره الثاني' ,
'ذل من لا سيف له' ,
'ذُلَّ من يغيظ الذليل بعيش' ,
'ذنبه على جنبه' ,
'ذو العقل يشقى بالنعيم بعقله وأخو الجهالة في الشقاوة ينعم' ,
'الذي لا يعرف الصقر يشويه' ,
'الذي لا يعرفك يجهلك' ,
'راحت السكرة وجاءت الفكرة' ,
'رأس الجهل الاغترار' ,
'رأس الحكمة مَخافةُ الله' ,
'رأس الخطايا الحرص والغضب' ,
'رأس العقل بعد الإيمان التودد إلى الناس' ,
'الرأي قبل شجاعة الشجعان' ,
'رأيت الناس قد مالوا إلى من عنده مال' ,
'رب أخ لم تلده أمي ينفي الأذى عني ويجلو همي' ,
'رب أخ لي لم تلده أمي ينفي الأذى عني ويجلو همي' ,
'رب بعيد أنفع من قريب' ,
'رب ثوب يستغيث من صاحبه' ,
'رب زارع لنفسه حاصد سواه' ,
'رب سكوت أبلغ من كلام' ,
'رب قول أشد من صول' ,
'رب كلام يثير الحروب' ,
'رب كلمة قالت لصاحبها دعني' ,
'رُبَّ دهر بكيت منه فلما صرت في غيره بكيت عليه' ,
'رُبَّ نعل شر من الحفا' ,
'ربك رب قلوب' ,
'ربما أراد الأحمق نفعك فضرك' ,
'الرجال بالأموال' ,
'رجع بخفي حنين' ,
'رجعت ريمة لعادتها القديمة' ,
'الرجوع إلى الحق خير من التمادي في الباطل' ,
'رِزْقُه في رجليه' ,
'الرفق بالجاني عتاب' ,
'الرمد أهون من العمى' ,
'رمية من غير رام' ,
'ريح صيف وطارق طيف' ,
'زرع آباؤنا فأكلنا ونزرع ليأكل أبناؤنا' ,
'زرعوا فأكلنا ونزرع فيأكلون' ,
'زعم الفرزدق أن سيقتل مربعاً أبشر بطول سلامة يا مربع' ,
'زمَّارُ الحي لا يُطْرِبُ' ,
'زيادة القول تحكي النقص في العمل ومنطق المرء قد يهديه للزلل' ,
'سائل البخيل محروم وماله مكتوم' ,
'سائل الله لا يخيب' ,
'سارت به الرُّكْبانُ' ,
'سافر تجد عوضا عما تفارقه' ,
'ساقي القوم آخرهم شراباً' ,
'الساكت عن الحق شيطان أخرس' ,
'سبق السيف العذل' ,
'ستبدي لك الأيام ما كنت جاهلا' ,
'سحابة صيف تذروها الرياح' ,
'سر النجاح على الدوام هو أن تسير إلى الأمام' ,
'السر أمانة' ,
'سرك أسيرك' ,
'السَّرْج المُذهَّب لا يجعلُ الحمار حصاناً' ,
'السعادة صحة جيدة وذاكرة سيئة' ,
'سفير السوء يفسد ذات البين' ,
'سكت دهرا ونطق كفرا' ,
'السكوت علامة الرضا' ,
'السلاح ثم الكفاح' ,
'سلامة الإنسان في حلاوة اللسان' ,
'السلطان من بَعُدَ عن السلطان' ,
'السماء لا تمطر ذهباً ولا فضة' ,
'سماعك بالْمُعَيْدِيِّ خير من أن تراه' ,
'سمك في ماء' ,
'سمن على عسل' ,
'سوء الخُلُق يُعْدِي' ,
'سيد القوم خادمهم' ,
'السيف أصدق أنباء من الكتب' ,
'سيف السلطان طويل' ,
'السيف أهول ما يُرى مسلولا' ,
'السيف يقطع بحده المرء يسعى بجده' ,
'شاور في أمرك الذين يخشون الله' ,
'شاور لبيباً ولا تعصه' ,
'شاور من جَرَّبَ' ,
'الشبعان يفُتُّ للجائع فتا بطيئا' ,
'شدة الألفة تزيل الكلفة' ,
'شدة وتزول' ,
'شر إخوانك من لا تعاتب' ,
'شر البلية ما يضحك' ,
'شر الحديث الكذب' ,
'شر السمك يكدر الماء' ,
'شر الناس من لا يبالي أن يراه الناس مسيئا' ,
'شر الوصل وصل لا يدوم' ,
'الشر في الناس لا يفنى وإن قُبِرُوا' ,
'الشر قليله كثير' ,
'الشر للشر خُلِقَ' ,
'الشرط نور' ,
'الشرير لا يظن بالناس خيراً' ,
'الشريف إذا تَقَوَّى تواضع والوضيع إذا تَقَوَّى تكبر' ,
'الشُّبْهَةُ أخت الحرام' ,
'شعيرنا ولا قمح غيرنا' ,
'شفيت نفسي ولكن جدعت أنفي' ,
'شق عصا الطاعة' ,
'شكرت جميل صنعكم بدمعي ودمع العين مقياس الشعور' ,
'الشكوى سلاح الضعفاء' ,
'الشكوى لغير الله مذلة' ,
'الشماتة بالمنكوب لؤم' ,
'شَمِّرْ وائتزر والبس جلد النمر' ,
'شنشنة أعرفها من أخزم' ,
'الشيب قبل العيب' ,
'صاحب إذا صاحبت كل ماجد سهل المحيا طلق مُسَاعِدِ' ,
'صاحب الحق عينه قوية' ,
'صاحب القرش صياد' ,
'الصباح رباح' ,
'الصبر صبران: صبر على ما تكره وصبر على ما تحب' ,
'الصبر عند الصدمة الأولى' ,
'الصبر مفتاح الفرج' ,
'صبرك عن محارم الله أيسر من صبرك على عذاب الله' ,
'صبري على نفسي ولا صبر الناس عليّ' ,
'صحبة السوء مفسدة للأخلاق' ,
'صدرك أوسع لسرك' ,
'الصدق دليل التقوى' ,
'الصدق يحسن بالفتى والكذب يحسب من عيوبه' ,
'صدور الأحرار قبور الأسرار' ,
'الصديق إما أن ينفع وإما أن يشفع' ,
'الصديق وقت الضيق' ,
'صديقك حين تستغنى كثير وما لك عند فقرك من صديق' ,
'الصِّيتُ ولا الغنى' ,
'صلاح أمرك بالأخلاق مرجعه فَقَوِّم النفس بالأخلاق تستقم' ,
'صلى وصام لأمر كان يأمله حتى قضاه فما صلى ولا صاما' ,
'صواب الجاهل كزلة العاقل' ,
'الضامن غارم' ,
'الضحك بلا سبب من قلة الأدب' ,
'ضرب أخماسا بأسداس' ,
'الضرب في الميت حرام' ,
'ضَرْبَة مُعَلِّمٍ' ,
'ضربني وبكى وسبقني واشتكى' ,
'الضرورات تبيح المحظورات' ,
'طاعة اللسان ندامة' ,
'الطبع غلب التطبع' ,
'طبيب يداوي الناس وهو عليل' ,
'طفح الكيل' ,
'طمع إبليس في الجنة' ,
'طول البال يهدم الجبال' ,
'الطيور على أشكالها تقع' ,
'ظاهر العتاب خير من باطن الحقد' ,
'الظَّفَرُ بالضعيف هزيمة' ,
'ظل السلطان سريع الزوال' ,
'الظلم أسرع شيء إلى تعجيل نقمة وتبديل نعمة' ,
'ظلم الأقارب أشد وقعا من السيف' ,
'الظلم مرتعه وخيم' ,
'ظن العاقل خير من يقين الجاهل' ,
'عاد الأمر إلى نصابه' ,
'العاقل لا يبطل حقا ولا يحق باطلا' ,
'العاقل لا يستقبل النعمة ببطر ولا يودعها بجزع' ,
'العاقل من عقل لسانه والجاهل من جهل قدره' ,
'عامل الناس برأي رفيق والق من تلقى بوجه طليق' ,
'عامل الناس بما تحب أن يعاملوك به' ,
'العبد يقرع بالعصا والحر تكفيه الإشارة' ,
'العتاب صابون القلب' ,
'العتاب قبل العقاب' ,
'العتاب هدية الأحباب' ,
'العتب على النظر' ,
'عثرة القدم أسلم من عثرة اللسان' ,
'العدد في الليمون' ,
'العدل أساس الْمُلْك' ,
'عدو عاقل خير من صديق جاهل' ,
'العديم من احتاج من اللئيم' ,
'عذر لم يتول الحق نسجه' ,
'العز في نواصي الخيل' ,
'عَزَّ من قنع وذل من طمع' ,
'عش رجبا ترى عجبا' ,
'عش عزيزا أو مت وأنت كريم' ,
'عصفور في اليد خير من عشرة على الشجرة' ,
'العفة جيش لايهزم' ,
'العفو عند المقدرة' ,
'العفو يصلح الكريم ويفسد اللئيم' ,
'العقل أشرف الأحباب' ,
'العقل زينة' ,
'العقل صدق الحكم على الأمور' ,
'العقل صفاء النفس والجهل كدرها' ,
'العقل غريزة تربيها التجارب' ,
'العقل يُهَابُ ما لا يُهابُ السيف' ,
'عقوبة الحاسد نفسه' ,
'عقول كل قوم على قَدْرِ زمانهم' ,
'علامة الكذاب جوده باليمين من غير مستحلف' ,
'العِلْمُ أشهر الأحساب' ,
'عِلْمُ الرجل ولده المخَلَّدُ' ,
'علم بلا عمل كشجر بلا ثمر' ,
'العلم زين فكن للعلم مكتسبا وكن له طالبا ما عشت مقتبسا' ,
'العلم في الصِّغَرِ كالنقش على الحجر' ,
'العلم كالسراج من مر به اقتبس منه' ,
'علم لا ينفع ككنز لا يُنْفَقُ منه' ,
'العلم يُؤْتَى ولا يَأْتِي' ,
'العلم يجدي ويبقى للفتى أبدا والمال يفنى وإن أجدى إلى حين' ,
'العلم يرفع بيتا لا عماد له والجهل يهدم بيت العز والشرف' ,
'العلماء ورثة الأنبياء' ,
'على الباغي تدور الدوائر' ,
'علي أن أسعى وليس علي إدراك النجاح' ,
'على رأسه ريشة' ,
'عليك بالإخوان فإنهم في الرخاء زينه وفي البلاء عُدَّةٌ' ,
'عليك بالجنة فإن النار في الكف' ,
'العمر واحد والرب واحد' ,
'العمل أبلغ خطابٍ' ,
'عمل البحر طحينة' ,
'عمى العين ولا عمى القلب' ,
'عن المرء لا تسأل وسل عن قرينه' ,
'عند الامتحان يكرم المرء أو يهان' ,
'عند البطون تعمى العيون' ,
'عند الرهان تعرف السوابق' ,
'عند الشدائد تعرف الإخوان' ,
'عند الصباح يحمد القوم السرى' ,
'عند جُهَيْنَةَ الخبر اليقين' ,
'عندما تغيب الهرة تلعب الفيران' ,
'عندما تكون في روما تصرف كما يتصرف الرومان' ,
'عنز استتيست' ,
'العنزة ترعى بمرعاها' ,
'العيش في الدنيا جهاد دائم' ,
'عيش وملح' ,
'العين بالعين والسن بالسن' ,
'العين لا تعلو على الحاجب' ,
'الغائب عُذْرُه معه' ,
'غاب حولين وجاء بِخُفَّيْ حنين' ,
'غابت السباع ولعبت الضباع' ,
'الغالي ثمنه فيه' ,
'غبن الصديق نذالة' ,
'الغريب أعمى ولو كان بصيراً' ,
'غضب الجاهل في قوله وغضب العاقل في فعله' ,
'الغضب صدأ العقل' ,
'غضبه على طرف أنفه' ,
'غنى المرء في الغربة وطن وفقره في الوطن غربة' ,
'غنى النفس خير من غنى المال' ,
'الغنى غنى القلب لا غنى المال' ,
'الغنى في يد اللئيم قبيح قدر قبح الكريم في الإملاق' ,
'الغنى يورث البطر' ,
'غيري يأكل الدجاج وأنا أقع في السياج' ,
'فاقد الشيء لا يعطيه' ,
'فالوجه مثل الصبح مبيض والشعر مثل الليل مسود' ,
'فإن قليل الحب بالعقل صالح وإن كثير الحب بالجهل فاسد' ,
'فت في عضد فلان' ,
'فخير ما كسبت إخوان الثقة أنس وعون في الأمور الموبقة' ,
'الفُرَصُ تَمُرُّ مَرَّ السحاب' ,
'فرط الأنس مكسبة لقرناء السوء' ,
'الفضل ما شهدت به الأعداء' ,
'الفقر ذل عليه باب مفتاحه العجز والتواني' ,
'فلان برق بلا مطر وشجر بلا ثمر' ,
'فلان بوجهين' ,
'فلان دُرَّةُ التاج وواسطة العقد' ,
'فلان قد ركب الفيل وقال لا تبصروني' ,
'فلان كالكعبة تُزارُ ولا تُسْتَزارُ' ,
'فلان يسرق الكحل من العين' ,
'فما تحمد العينان كل بشاشة ولا كل وجه عابس بذميم' ,
'فوا عجبا كم يدعي الفضل ناقص ووا أسفا كم يدعي النقص فاضل' ,
'فوت الحاجة خير من طلبها إلى غير أهلها' ,
'في التأني السلامة وفي العجلة الندامة' ,
'في التجارب علم مستأنف' ,
'في الجريرة تشترك العشيرة' ,
'في الشدائد يعرف الإخوان' ,
'في تقلب الأحوال علم جواهر الرجال' ,
'في سعة الأخلاق كنوز الأرزاق' ,
'في فمي ماء وهل ينطق من في فمه ماء' ,
'فيا ليت الشباب يعود يوما فأخبره بما فعل المشيب' ,
'فيا موقدا نارا لغيرك ضوؤها' ,
'قد أعذر من أنذر' ,
'قد يتوقى السيف وهو مغمد' ,
'قد يجبن الشجاع بلا سلاح' ,
'قد يجمع المال غير آكله ويأكل المال غير من جمعه' ,
'قد يخرج من الصدفة غير الدُّرَّة' ,
'قد يخلق من ظهر العالم جاهلاً' ,
'قد يدرك المتأني بعض حاجته وقد يكون مع المستعجل الزلل' ,
'قد ينبت الشوك وسط الزهور' ,
'قَدِّرْ لِرِجْلِكَ قبل الخطو موضعها' ,
'القِدْر الكبير يتسع للكبير' ,
'القدوة الحسنة خير من النصيحة' ,
'القدوة الحسنة خير من الوصية' ,
'قرة عين' ,
'القرد في عين أمه غزال' ,
'القرش الأبيض ينفع في اليوم الأسود' ,
'القشة التي قصمت ظهر البعير' ,
'القَصَّابُ لا تهوله كثرة الغنم' ,
'قضى نحبه' ,
'قلب المؤمن دليله' ,
'قلب له ظهر المِجَنِّ' ,
'القلة ذلة' ,
'قليل المال تصلحه فيبقى ولا يبقى الكثير مع الفساد' ,
'قليل دائم خير من كثير منقطع' ,
'قليل في الجيب خير من كثير في الغيب' ,
'قم للمعلم وفه التبجيلا كاد المعلم أن يكون رسولا' ,
'القناعة كنز لا يفنى' ,
'قول الحق لم يدع لي صديقا' ,
'قيل للبغل: "من أبوك" قال "الفرس خالي"' ,
'قَيِّدُوا العلم بالكتابة' ,
'قَيِّدُوا نعم الله بالشكر' ,
'كاد الفقر أن يكون كفراً' ,
'كالإبرة تكسي غيرها وهي عريانة' ,
'كالأطرش في الزَّفَّة' ,
'كالجراد: لا يبقى ولا يذر' ,
'كالحادي وليس له بعير' ,
'كالذئب: إذا طلب هرب وإذا تمكن وثب' ,
'كالضريع لا يسمن ولا يغني من جوع' ,
'كالقابض على الماء' ,
'كالمحتمي ببيت العنكبوت' ,
'كالمستجير من الرمضاء بالنار' ,
'كالنحل: في أفواهها عسل يحلو وفي أذنابها السم' ,
'كالنعامة: لا تطير ولا تحمل' ,
'كأن الحاسد إنما خلق ليغتاظ' ,
'كأن الشمس تطلع من حرامه' ,
'كأن على رءوسهم الطير' ,
'الكتاب يقرأ من عنوانه' ,
'كثرة الضحك تذهب الهيبة' ,
'كثرة العتاب تفرق الأحباب' ,
'كثرة العتاب تورث البغضاء' ,
'الكذب داء والصدق دواء' ,
'كذلك غمر الماء يروي ويغرق' ,
'كرامة العبد من كرامة سيده' ,
'كريشة في مهب الريح' ,
'الكريم من أكرم الأحرار' ,
'الكريم يظلم من فوقه واللئيم يظلم من تحته' ,
'كطالب الصيد في عرين الأسد' ,
'كعبة الله لا تكسى لإعواز' ,
'كفى المرء فضلا أن تُعَدَّ معايبه' ,
'كل ابن أنثى وإن طالت سلامته يوماً على آلة حدباء محمول' ,
'كل آت قريب' ,
'كل امرئ بما يحسنه' ,
'كل إناء بالذي فيه ينضح' ,
'كل بؤس وكل نعيم زائل' ,
'كل حبل على غاربه' ,
'كل ذات ذيل تختال' ,
'كل رأس به صُداع' ,
'كل زائد ناقص' ,
'كل سر جاوز الاثنين شاع' ,
'كل شيء يختال فيه الرجال غير أن ليس للمنايا احتيال' ,
'كل غريب للغريب نسيب' ,
'كل كلب ببابه ينبح' ,
'كل ما تشتهي والبس ما يشتهي الناس' ,
'كل ما في البلاد من أموال ليس إلا نتيجة الأعمال' ,
'كل مبذول مملول' ,
'كل ممنوع مرغوب' ,
'كل هم إلى فرج' ,
'كل واحد له قادح ومادح' ,
'الكلاب النباحة نادراً ما تعض' ,
'الكلاب تنبح والقافلة تسير' ,
'كلام الليل يمحوه النهار' ,
'كلام كالعسل ووغزٌ كالأسل' ,
'كلب جَوَّالٌ خير من أسد رابض' ,
'كلكم طلب صيد' ,
'كلما طار قص جناحه' ,
'كلما كثر الذباب هان قتله' ,
'كم من كثير العلم والوفاء قد صانه العقل عن الرياء' ,
'كما أن السؤال يُذِلُّ قوما كذاك يعز قوم بالعطاء' ,
'كما تدين تدان' ,
'كما تزرع تحصد' ,
'كمن يربي الذئب' ,
'كن دافنا للشر بالخير تسترح من الهم' ,
'كن لينا من غير ضعف وشديدا من غير عنف' ,
'كن لَيِّنًا في غير ضعف وشديداً في غير عنف' ,
'كناطح صخرة يوما ليكسرها فلم يضرها وأوهى قرنه الوعل' ,
'كهرة تأكل أولادها' ,
'ا بد دون الشهد من إبر النحل' ,
'لا بد للمصدور من أن ينفث' ,
'لا تؤجل عمل اليوم إلى الغد' ,
'لا تأكل خبزك على مائدة غيرك' ,
'لا تأمن من كذب لك أن يكذب عليك' ,
'لا تبع نقداً بدين' ,
'لا تبع يوماً صالحاً بيوم طالح' ,
'لا تجعلن دليل المرء صورته' ,
'لا تجن يمينك على شمالك' ,
'لا تحسبن العلم ينفع وحده ما لم يتوج ربه بخلاق' ,
'لا تخاصم من إذا قال فعل' ,
'لا تُرَخِّص الضرورة بالإلحاح' ,
'لا ترم سهما يعسر عليك رده' ,
'لا تسقط من كفه خردلة' ,
'لا تشكون إلى خلق فتشمته شكوى الجريح إلى الغربان والرخم' ,
'لا تشن وجه العفو بالتأنيب' ,
'لا تطلقن القول في غير بصر إن اللسان غير مأمون الضرر' ,
'لا تعنف طالبا لرزقه' ,
'لا تقطعن ذنب الأفعى وترسلها إن كنت شهما فأتبع رأسها الذنبا' ,
'لا تكن حلواً فتؤكل ولا مراً فترمى' ,
'لا تكن رأسا فالرأس كثير الأذى' ,
'لا تكن رطبا فَتُعْصَرَ ولا يابسا فتكسر' ,
'لا تلتقي الجبال' ,
'لا تلم المفشي إليك سرا وأنت قد ضقت بذاك صدرا' ,
'لا تَلُمْ كفي إذا السيف نبا صح مِنِّي العزم والدهر أبى' ,
'لا تمازح الشريف فيحنق عليك ولا الدنيء فيتجرأ عليك' ,
'لا تمدّن إلى المعالي يدا قصرت عن المعروف' ,
'لا تنه عن خُلُقٍ وتأتي مثله عار عليك إذا فعلت عظيم' ,
'لا تهرف بما لا تعرف' ,
'لا جدوى من البكاء على اللبن المسكوب' ,
'لا جديد تحت الشمس' ,
'لا جُرْمَ بعد الندامة' ,
'لا حذر من قدر' ,
'لا حر بوادي عوف' ,
'لا حي فيرجى ولا ميت فينسى' ,
'لا خير فيمن لا يَأْلَفُ ولا يؤلف' ,
'لا خير فيمن لا يدوم له أحد' ,
'لا راحة لحسود' ,
'لا رأي لكذوب' ,
'لا رأي لمن لا يطاع' ,
'لا رسول كالدرهم' ,
'لا طال توت الشام ولا عنب اليمن' ,
'دع الأيام تفعل ما تشاء وطب نفسا بما حكم القضاء' ,
'وما نيل المطالب بالتمني ولكن تؤخذ الدنيا غلابا' ,
'الحق يعلو ولا يعلى عليه' ,
'ولا خير في حسن الجسوم وطولها إذا لم يزن طول الجسوم عقول' ,
'جمال السماء في نجومها وجمال المرأة في شعرها' ,
'أصفى من الدمعة' ,
'أصحابي كالنجوم بأيهم اقتديتم اهتديتم' ,
'بريء منها براءة الذئب من دم ابن يعقوب' ,
'إذا تفرقت الغنم قادتها العنز الجرباء' ,
'آفة الحديث الكذب' ,
'أطول من ليل الشتاء' ,
'الظلم مرتعه وخيم' ,
'ضربني وبكى وسبقني واشتكى' ,
'مرآة الحب عمياء' ,
'فيا ليت الشباب يعود يوما فأخبره بما فعل المشيب' ,
'من يغرق يتعلق بعود قش' ,
'بيت الظالم خراب' ,
'الأفعال أبلغ من الأقوال' ,
'ازرع كل يوم تأكل' ,
'اختلط حابلهم بنابلهم' ,
'حبل الكذب قصير' ,
'البعد جفاء' ,
'حيلة العاجز دموعه' ,
'ظلم الأقارب أشد وقعا من السيف' ,
'نوم الظالم عبادة' ,
'إن الله يمهل ولا يهمل' ,
'أعلمه الرماية فلما أشتد ساعِدُهُ رماني' ,
'جنت على نفسها براقش' ,
'اشتر من بيت الغنى جوادا ومن بيت الفقير زوجة' ,
'أغنى الأغنياء من لم يكن للبخل أسيراً' ,
'مصائب قوم عند قوم فوائد' ,
'تجري الرياح بما لا تشتهي السفن' ,
'إن غدا لناظره قريب' ,
'الغريب أعمى ولو كان بصيراً' ,
'لا تؤجل عمل اليوم إلى الغد' ,
'من جد وجد ومن زرع حصد' ,
'رُبَّ دهر بكيت منه فلما صرت في غيره بكيت عليه' ,
'من طلب العلا سهر الليالي' ,
'تقطع أعناق الرجال المطامع' ,
'من طلب شيئا وجده' ,
'أرفع من السماء' ,
'أسرع من الطرف' ,
'كن لينا من غير ضعف وشديدا من غير عنف' ,
'إذا أتاك أحد الخصمين وقد فُقِئَتْ عينه فلا تقض له حتى يأتيك خصمه فلعله قد فُقِئَتْ عيناه' ,
'أبعد من الثريا' ,
'إذا كنت تعلم فتلك مصيبة وإن كنت لا تعلم فالمصيبة أعظم' ,
'حافٍ يسخر بناعل' ,
'أزهى من طاووس' ,
'شر البلية ما يضحك' ,
'أرق من النسيم' ,
'لسانك حصانك ان صنته صانك وان هنته هانك' ,
'الجوع كافر' ,
'الناس سواسية كأسنان المشط' ,
'أبصر من زرقاء اليمامة' ,
'تأبي الرماح إذا اجتمعن تكسرا وإذا افترقن تكسرت أفرادا' ,
'الحرب سجال' ,
'أسرع من البرق' ,
'تمخض الجبل فولد فأرا' ,
'أذا كان رب البيت على الدف ناقر فشيمة أهل البيت الرقص' ,
'الجهل موت الأحياء' ,
'الصبر مفتاح الفرج' ,
'خير الكلام ما قل ودل' ,
'حفظ السر أمانة' ,
'أول الغضب جنون وآخره ندم' ,
'ينبت الشوك وسط الزهور' ,
'لا تناطح بقرون من فخار' ,
'لكل جواد كبوة' ,
'اعمل لدنياك كأنك تعيش ابداً واعمل لآخرتك كأنك تموت غداً' ,
'اذا فعلت شيئاً فكن كمن لم يفعل شيئاً' ,
'البخيل غناه فقر ومطبخه قفر' ,
'المكر حيلة من لا حيلة له' ,
'أياك وأن يضرب لسانك عنقك' ,
'عش عزيزا أو مت وأنت كريم' ,
'سلامة الإنسان في حلاوة اللسان' ,
'كلمة لا لا متلها طباً و لا دواء' ,
'المتكبر كالواقف على الجبل يرى الناس صغاراً ويرونه صغيراً' ,
'إذا ظلمت من دونك فلا تأمن عقاب من فوقك' ,
'عامل الناس بما تحب أن يعاملوك به' ,
'ذل من لا سيف له']