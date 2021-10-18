def erro(x):
	try:
		eval(x)

	except ValueError as e:
		print(type(e))	# instância da exceção
		print(e.args)	# argumentos das mensagens
		print(e)		# __str__ da mensagem

	except ZeroDivisionError:
		print("ZeroDivisionError ocorreu")

	except(TypeError, NameError):
		print("TypeError ou NameError ocorreu")

	else: #Entra aqui quando o try é executado com sucesso
		print("Nenhuma exceção ocorreu")

	finally: #Essa instrução é executada independente de exceções serem levantadas ou não
			 #Se ocorrer uma exceção que não foi tratada, o cursor executará o finally também
		print("Sempre será executado")

#ValueError:
erro("int('a')")

#ZeroDivisionError:
erro("10/0")

#TypeError:
erro("int+int")

#NameError:
erro("a")

erro("10+10")