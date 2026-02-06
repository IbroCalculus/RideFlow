import 'package:dio/dio.dart';
import 'package:riverpod_annotation/riverpod_annotation.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../../core/api_client.dart';

part 'auth_repository.g.dart';

@riverpod
AuthRepository authRepository(AuthRepositoryRef ref) {
  return AuthRepository(ref.watch(apiClientProvider));
}

class AuthRepository {
  final Dio _dio;
  AuthRepository(this._dio);

  Future<void> login(String email, String password) async {
    try {
      final response = await _dio.post(
        '/auth/token',
        data: {'username': email, 'password': password},
        options: Options(contentType: Headers.formUrlEncodedContentType),
      );

      final token = response.data['access_token'];
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString('access_token', token);
    } catch (e) {
      throw Exception('Login failed: $e');
    }
  }

  Future<void> register(
    String email,
    String password,
    String phone,
    String name,
    bool isDriver,
  ) async {
    try {
      await _dio.post(
        '/auth/register',
        data: {
          'email': email,
          'password': password,
          'phone_number': phone,
          'full_name': name,
          'is_driver': isDriver,
        },
      );
    } catch (e) {
      throw Exception('Registration failed: $e');
    }
  }
}
